// Motor de Gamificação do Hub SEFAZ (100% localStorage, sem backend)
// Autor: Jarbas (YLuna85 LABs)

const GAMIF_STORAGE_KEY = "sefaz_gamificacao_v1";
const GAMIF_REVIEW_INTERVALS = [1, 3, 7, 30];

const BADGES_CATALOGO = {
  primeiro_passo: { nome: "Primeiro Passo", desc: "Marcou o primeiro tópico de estudo.", icone: "fa-shoe-prints" },
  apostila_completa: { nome: "Apostila Concluída", desc: "Concluiu 100% de uma matéria em alguma trilha.", icone: "fa-book-circle-check" },
  trilha_completa: { nome: "Trilha Completa", desc: "Concluiu 100% de uma trilha inteira de estudos.", icone: "fa-flag-checkered" },
  sequencia_3: { nome: "Sequência de 3 Dias", desc: "Estudou 3 dias seguidos.", icone: "fa-fire" },
  sequencia_7: { nome: "Sequência de 7 Dias", desc: "Estudou 7 dias seguidos.", icone: "fa-fire-flame-curved" },
  sequencia_30: { nome: "Sequência de 30 Dias", desc: "Estudou 30 dias seguidos.", icone: "fa-fire-flame-simple" },
  simulado_10: { nome: "Primeiras 10 Questões", desc: "Respondeu 10 questões de simulado.", icone: "fa-pen" },
  simulado_100: { nome: "Maratonista de Questões", desc: "Respondeu 100 questões de simulado.", icone: "fa-medal" },
  sem_erro_10: { nome: "Sequência Perfeita", desc: "Acertou 10 questões seguidas em um simulado.", icone: "fa-bullseye" },
  revisor_dedicado: { nome: "Revisor Dedicado", desc: "Zerou a fila de revisão espaçada.", icone: "fa-rotate" }
};

const NIVEIS_LABEL = ["Iniciante", "Aprendiz", "Aplicado", "Consistente", "Avançado", "Especialista", "Referência", "Mestre Fiscal"];

function gamifDefaultState() {
  return {
    xpTotal: 0,
    xpPorMateria: {},
    topicosComXp: [],
    streak: { atual: 0, recorde: 0, ultimoDia: null },
    badges: [],
    filaRevisao: {},
    stats: { questoesRespondidas: 0, acertos: 0, acertosSeguidos: 0, melhorSequenciaAcertos: 0 },
    eventosPendentes: []
  };
}

function gamifLoad() {
  try {
    const raw = localStorage.getItem(GAMIF_STORAGE_KEY);
    if (!raw) return gamifDefaultState();
    const parsed = JSON.parse(raw);
    return Object.assign(gamifDefaultState(), parsed);
  } catch (e) {
    console.error("Erro ao ler dados de gamificação:", e);
    return gamifDefaultState();
  }
}

function gamifSave(state) {
  localStorage.setItem(GAMIF_STORAGE_KEY, JSON.stringify(state));
}

function gamifHoje() {
  return new Date().toISOString().slice(0, 10);
}

function gamifDiasEntre(dataA, dataB) {
  const a = new Date(dataA + "T00:00:00");
  const b = new Date(dataB + "T00:00:00");
  return Math.round((b - a) / 86400000);
}

// Nível calculado por progressão: nível N exige 100 * N * (N+1) / 2 de XP acumulado
function gamifCalcularNivel(xpTotal) {
  let nivel = 1;
  while (100 * nivel * (nivel + 1) / 2 <= xpTotal) {
    nivel++;
  }
  const xpNivelAtual = 100 * (nivel - 1) * nivel / 2;
  const xpProximoNivel = 100 * nivel * (nivel + 1) / 2;
  const label = NIVEIS_LABEL[Math.min(nivel - 1, NIVEIS_LABEL.length - 1)];
  return {
    nivel,
    label,
    xpNivelAtual,
    xpProximoNivel,
    progressoPct: Math.round(((xpTotal - xpNivelAtual) / (xpProximoNivel - xpNivelAtual)) * 100)
  };
}

function gamifAdicionarXp(state, quantidade, materia) {
  state.xpTotal += quantidade;
  if (materia) {
    state.xpPorMateria[materia] = (state.xpPorMateria[materia] || 0) + quantidade;
  }
}

function gamifConcederBadge(state, badgeId) {
  if (!state.badges.includes(badgeId)) {
    state.badges.push(badgeId);
    state.eventosPendentes.push({ tipo: "badge", badgeId });
  }
}

// Chamado uma vez a cada abertura do app para atualizar a sequência de dias
function gamifAtualizarStreak(state) {
  const hoje = gamifHoje();
  if (state.streak.ultimoDia === hoje) return;

  if (!state.streak.ultimoDia) {
    state.streak.atual = 1;
  } else {
    const diff = gamifDiasEntre(state.streak.ultimoDia, hoje);
    if (diff === 1) {
      state.streak.atual += 1;
    } else if (diff > 1) {
      state.streak.atual = 1;
    }
  }
  state.streak.ultimoDia = hoje;
  state.streak.recorde = Math.max(state.streak.recorde, state.streak.atual);

  if (state.streak.atual >= 3) gamifConcederBadge(state, "sequencia_3");
  if (state.streak.atual >= 7) gamifConcederBadge(state, "sequencia_7");
  if (state.streak.atual >= 30) gamifConcederBadge(state, "sequencia_30");
}

// Chamado quando um tópico de trilha é marcado ou desmarcado
function gamifOnTopicToggle(topicId, checked, materiaId) {
  const state = gamifLoad();
  gamifAtualizarStreak(state);

  if (checked && !state.topicosComXp.includes(topicId)) {
    state.topicosComXp.push(topicId);
    gamifAdicionarXp(state, 10, materiaId || "geral");
    if (state.topicosComXp.length === 1) gamifConcederBadge(state, "primeiro_passo");
  }

  gamifSave(state);
  gamifRenderWidget();
  return state;
}

// Verifica se uma matéria ou trilha inteira chegou a 100% e concede badge (chamado externamente com a % calculada)
function gamifOnMateriaCompleta() {
  const state = gamifLoad();
  gamifConcederBadge(state, "apostila_completa");
  gamifSave(state);
  gamifRenderWidget();
}

function gamifOnTrilhaCompleta() {
  const state = gamifLoad();
  gamifConcederBadge(state, "trilha_completa");
  gamifSave(state);
  gamifRenderWidget();
}

// Chamado a cada resposta de questão do simulado
function gamifOnQuizAnswer(questionId, materiaId, acertou) {
  const state = gamifLoad();
  gamifAtualizarStreak(state);

  state.stats.questoesRespondidas += 1;
  if (acertou) {
    state.stats.acertos += 1;
    state.stats.acertosSeguidos += 1;
    state.stats.melhorSequenciaAcertos = Math.max(state.stats.melhorSequenciaAcertos, state.stats.acertosSeguidos);
    gamifAdicionarXp(state, 15, materiaId || "geral");
  } else {
    state.stats.acertosSeguidos = 0;
    gamifAdicionarXp(state, 2, materiaId || "geral");
  }

  gamifAtualizarFilaRevisao(state, questionId, materiaId, acertou);

  if (state.stats.questoesRespondidas === 10) gamifConcederBadge(state, "simulado_10");
  if (state.stats.questoesRespondidas === 100) gamifConcederBadge(state, "simulado_100");
  if (state.stats.acertosSeguidos === 10) gamifConcederBadge(state, "sem_erro_10");

  gamifSave(state);
  gamifRenderWidget();
  return state;
}

function gamifAtualizarFilaRevisao(state, questionId, materiaId, acertou) {
  const hoje = gamifHoje();
  const item = state.filaRevisao[questionId];

  if (!acertou) {
    state.filaRevisao[questionId] = { materiaId: materiaId || "geral", intervaloIdx: 0, dueDate: gamifSomarDias(hoje, GAMIF_REVIEW_INTERVALS[0]) };
    return;
  }

  if (item) {
    const proximoIdx = item.intervaloIdx + 1;
    if (proximoIdx >= GAMIF_REVIEW_INTERVALS.length) {
      delete state.filaRevisao[questionId];
      if (Object.keys(state.filaRevisao).length === 0) gamifConcederBadge(state, "revisor_dedicado");
    } else {
      state.filaRevisao[questionId] = { materiaId: item.materiaId, intervaloIdx: proximoIdx, dueDate: gamifSomarDias(hoje, GAMIF_REVIEW_INTERVALS[proximoIdx]) };
    }
  }
}

function gamifSomarDias(dataBase, dias) {
  const d = new Date(dataBase + "T00:00:00");
  d.setDate(d.getDate() + dias);
  return d.toISOString().slice(0, 10);
}

// Retorna a lista de ids de questões vencidas (prontas para revisão hoje)
function gamifIdsParaRevisarHoje() {
  const state = gamifLoad();
  const hoje = gamifHoje();
  return Object.keys(state.filaRevisao).filter(qid => state.filaRevisao[qid].dueDate <= hoje);
}

function gamifContarFilaRevisao() {
  return Object.keys(gamifLoad().filaRevisao).length;
}

// Renderiza o widget de progresso no Painel Geral (bento card, sem sidestripe)
function gamifRenderWidget() {
  const container = document.getElementById("gamificacao-widget");
  if (!container) return;

  const state = gamifLoad();
  const nivelInfo = gamifCalcularNivel(state.xpTotal);
  const filaCount = Object.keys(state.filaRevisao).length;

  const badgesHtml = Object.keys(BADGES_CATALOGO).map(id => {
    const conquistado = state.badges.includes(id);
    const b = BADGES_CATALOGO[id];
    return `
      <div class="badge-chip ${conquistado ? "badge-earned" : "badge-locked"}" title="${escapeHtml(b.desc)}">
        <i class="fa-solid ${b.icone}"></i>
        <span>${escapeHtml(b.nome)}</span>
      </div>
    `;
  }).join("");

  container.innerHTML = `
    <div class="gamif-header-row">
      <div class="gamif-level-block">
        <span class="gamif-level-num">Nível ${nivelInfo.nivel}</span>
        <span class="gamif-level-label">${escapeHtml(nivelInfo.label)}</span>
      </div>
      <div class="gamif-streak-pill">
        <span class="status-indicator-dot dot-orange"></span>
        <i class="fa-solid fa-fire"></i> ${state.streak.atual} dia${state.streak.atual === 1 ? "" : "s"} seguidos
      </div>
    </div>
    <div class="gamif-xp-bar-container">
      <div class="gamif-xp-bar" style="width:${Math.min(nivelInfo.progressoPct, 100)}%"></div>
    </div>
    <div class="gamif-xp-caption">${state.xpTotal} XP total &middot; ${nivelInfo.xpProximoNivel - state.xpTotal} XP para o próximo nível</div>
    <div class="gamif-badges-row">${badgesHtml}</div>
    ${filaCount > 0 ? `
      <div class="gamif-review-alert">
        <span class="status-indicator-dot dot-cyan"></span>
        ${filaCount} questão${filaCount === 1 ? "" : "ões"} na fila de revisão espaçada.
        <button class="gamif-review-btn" onclick="startRevisaoEspacada()">Revisar agora</button>
      </div>
    ` : ""}
  `;
}

// Dispara um toast simples para XP ganho ou badge desbloqueada (usa a área de eventos pendentes)
function gamifProcessarEventosPendentes() {
  const state = gamifLoad();
  if (!state.eventosPendentes || state.eventosPendentes.length === 0) return;

  state.eventosPendentes.forEach(evento => {
    if (evento.tipo === "badge") {
      const b = BADGES_CATALOGO[evento.badgeId];
      if (b) gamifMostrarToast(`Conquista desbloqueada: ${b.nome}`, b.icone);
    }
  });

  state.eventosPendentes = [];
  gamifSave(state);
}

function gamifMostrarToast(mensagem, icone) {
  const toast = document.createElement("div");
  toast.className = "gamif-toast";
  toast.innerHTML = `<i class="fa-solid ${icone || "fa-star"}"></i> ${escapeHtml(mensagem)}`;
  document.body.appendChild(toast);
  requestAnimationFrame(() => toast.classList.add("gamif-toast-visible"));
  setTimeout(() => {
    toast.classList.remove("gamif-toast-visible");
    setTimeout(() => toast.remove(), 400);
  }, 3200);
}

function gamifOnAppOpen() {
  const state = gamifLoad();
  const streakAnterior = state.streak.atual;
  gamifAtualizarStreak(state);
  gamifSave(state);
  gamifRenderWidget();
  if (state.streak.atual !== streakAnterior) {
    setTimeout(gamifProcessarEventosPendentes, 600);
  } else {
    gamifProcessarEventosPendentes();
  }
}
