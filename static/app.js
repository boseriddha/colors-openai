const form = document.querySelector("#form");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  getColors();
});

function getColors() {
  const query = form.elements.query.value;
  fetch("/palette", {
    method: "POST",
    headers: {
      "Content-type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      query: query,
    }),
  }).then((res) => {
    res.json().then((data) => {
      const colors = data.colors;
      const container = document.querySelector(".container");
      container.replaceChildren([]);
      createColors(colors, container);
    });
  });
}

function createColors(colors, parent) {
  parent.innerHTML = "";
  for (const color of colors) {
    const div = document.createElement("div");
    div.classList.add("color");
    div.style.backgroundColor = color;
    const width = 100 / colors.length;
    div.style.width = `${width}%`;

    div.addEventListener("click", () => {
      navigator.clipboard.writeText(color);
    });

    const span = document.createElement("span");
    span.innerText = color;

    div.appendChild(span);

    parent.appendChild(div);
  }
}
