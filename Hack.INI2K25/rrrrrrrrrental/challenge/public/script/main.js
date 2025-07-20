let page = 0;
let loading = false;
let allLoaded = false;

async function loadMoreCars() {
  if (loading || allLoaded) return;
  loading = true;
  const res = await fetch(`/static/cars.json?page=${page}`);
  const data = await res.json();

  if ((data.length === 1) && (data[0] == 'done')) {
    document.getElementById('loader').innerText = 'All cars loaded.';
    allLoaded = true;
    document.getElementById('fetchFeature').style.display = 'flex';
    return;
  }

  const carsDiv = document.getElementById('cars');
  data.forEach(car => {
    const div = document.createElement('div');
    div.className = 'car';
    div.innerHTML = `
      <img src="${car.image}" alt="${car.title}" />
      <h3>${car.title}</h3>
      <p><strong>Started:</strong> ${car.start_production}</p>
      <p><strong>Class:</strong> ${car.class}</p>
    `;
    carsDiv.appendChild(div);
  });

  page++;
  loading = false;
}

window.onscroll = () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
    loadMoreCars();
  }
};

document.getElementById('fetchFeature').onclick = async () => {
  const res = await fetch('/features/feature.json');
  const text = await res.text();
  document.getElementById('featureOutput').innerText = text;
};

navigator.serviceWorker.register('/sw.js');
loadMoreCars();