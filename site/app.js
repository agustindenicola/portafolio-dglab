// Interacciones de la portada. Todo es opcional: sin JS la pagina se ve completa.
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// Aparicion suave al hacer scroll.
const revealer = "IntersectionObserver" in window
  ? new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("visible");
          revealer.unobserve(entry.target);
        });
      },
      { threshold: 0.12 },
    )
  : null;
document.querySelectorAll(".reveal").forEach((el) => (revealer ? revealer.observe(el) : el.classList.add("visible")));

// Frase rotativa del titulo.
document.querySelectorAll(".rotator").forEach((rotator) => {
  const words = rotator.dataset.words.split("|");
  const word = rotator.querySelector(".rotator-word");
  if (reduceMotion || words.length < 2) return;
  let index = words.length - 1;
  setInterval(() => {
    index = (index + 1) % words.length;
    word.classList.add("out");
    setTimeout(() => {
      word.textContent = words[index];
      word.classList.remove("out");
    }, 280);
  }, 2400);
});

// Contadores.
document.querySelectorAll("[data-count]").forEach((el) => {
  const target = Number(el.dataset.count);
  if (reduceMotion || !revealer) return;
  const run = new IntersectionObserver((entries) => {
    if (!entries[0].isIntersecting) return;
    run.disconnect();
    const start = performance.now();
    const tick = (now) => {
      const t = Math.min(1, (now - start) / 1100);
      el.textContent = Math.round(target * (1 - Math.pow(1 - t, 3)));
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  });
  run.observe(el);
});

// Comparador antes / despues.
document.querySelectorAll(".compare").forEach((box) => {
  const range = box.querySelector(".compare-range");
  const set = (value) => box.style.setProperty("--pos", `${value}%`);
  range.addEventListener("input", () => set(range.value));
  // "Antes" muestra todo el Excel y "Despues" todo el sistema, con animacion.
  box.querySelectorAll("[data-go]").forEach((button) => {
    button.addEventListener("click", () => {
      box.dataset.stopHint = "1";
      delete box.dataset.touched;
      range.value = button.dataset.go;
      set(button.dataset.go);
    });
  });
  if (reduceMotion || !revealer) return;
  // Pista: la barra se mueve sola una vez para mostrar que se puede arrastrar.
  const hint = new IntersectionObserver((entries) => {
    if (!entries[0].isIntersecting) return;
    hint.disconnect();
    const frames = [50, 72, 28, 50];
    let i = 0;
    const step = () => {
      if (i >= frames.length || box.dataset.touched || box.dataset.stopHint) return;
      range.value = frames[i];
      set(frames[i]);
      i += 1;
      setTimeout(step, 650);
    };
    setTimeout(step, 400);
  }, { threshold: 0.5 });
  hint.observe(box);
  range.addEventListener("pointerdown", () => (box.dataset.touched = "1"));
});

// Tarjetas que se inclinan apenas con el mouse.
if (!reduceMotion && window.matchMedia("(hover: hover)").matches) {
  document.querySelectorAll("[data-tilt]").forEach((card) => {
    card.addEventListener("mousemove", (event) => {
      const r = card.getBoundingClientRect();
      const x = (event.clientX - r.left) / r.width - 0.5;
      const y = (event.clientY - r.top) / r.height - 0.5;
      card.style.setProperty("--rx", `${(-y * 4).toFixed(2)}deg`);
      card.style.setProperty("--ry", `${(x * 5).toFixed(2)}deg`);
      card.style.setProperty("--mx", `${((x + 0.5) * 100).toFixed(1)}%`);
      card.style.setProperty("--my", `${((y + 0.5) * 100).toFixed(1)}%`);
    });
    card.addEventListener("mouseleave", () => {
      card.style.setProperty("--rx", "0deg");
      card.style.setProperty("--ry", "0deg");
    });
  });
}

// "Contanos tu caso": arma el mensaje de WhatsApp con lo que el cliente toca.
const builder = document.querySelector("#consulta");
if (builder) {
  const preview = document.querySelector("#consulta-preview");
  const send = document.querySelector("#consulta-enviar");
  const detail = document.querySelector("#consulta-detalle");
  const name = document.querySelector("#consulta-nombre");
  const selected = (group) =>
    [...builder.querySelectorAll(`[data-group="${group}"] .choice.on`)].map((button) => button.dataset.value);
  const listar = (items) => (items.length > 1 ? `${items.slice(0, -1).join(", ")} y ${items[items.length - 1]}` : items[0] || "");
  const update = () => {
    const rubro = selected("rubro")[0];
    const necesidades = selected("necesidad").map((item) => item.charAt(0).toLowerCase() + item.slice(1));
    const partes = [`¡Hola DGLab!${name.value.trim() ? ` Soy ${name.value.trim()}.` : ""}`];
    if (rubro === "Gobierno") partes.push("Les escribo desde un organismo de gobierno.");
    else if (rubro && rubro !== "Otro") partes.push(`Mi negocio es del rubro ${rubro.toLowerCase()}.`);
    partes.push(necesidades.length ? `Me interesa: ${listar(necesidades)}.` : "Vi tu página y quería consultar por un proyecto.");
    if (detail.value.trim()) partes.push(`Hoy: ${detail.value.trim()}`);
    const mensaje = partes.join(" ");
    preview.textContent = mensaje;
    send.href = `https://wa.me/${builder.dataset.whatsapp}?text=${encodeURIComponent(mensaje)}`;
    // Para las estadisticas: que rubro eligio quien toca "Enviar".
    send.dataset.umamiEventRubro = rubro || "sin elegir";
  };
  builder.querySelectorAll(".choices").forEach((group) => {
    group.addEventListener("click", (event) => {
      const button = event.target.closest(".choice");
      if (!button) return;
      if (group.hasAttribute("data-single")) {
        group.querySelectorAll(".choice").forEach((other) => other !== button && other.classList.remove("on"));
      }
      button.classList.toggle("on");
      button.setAttribute("aria-pressed", button.classList.contains("on"));
      update();
    });
  });
  [detail, name].forEach((field) => field.addEventListener("input", update));
  builder.addEventListener("submit", (event) => event.preventDefault());
  update();
}

// "Ver todos los proyectos": despliega las tarjetas ocultas.
document.querySelectorAll("[data-more]").forEach((button) => {
  const grid = document.getElementById(button.dataset.more);
  button.addEventListener("click", () => {
    grid.classList.add("open");
    grid.querySelectorAll(".reveal").forEach((el) => el.classList.add("visible"));
    button.parentElement.remove();
  });
});
