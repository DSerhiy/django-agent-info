(async function () {

  const COUNTRY_ENDPOINT = 'http://127.0.0.1:8000/json-country';
  const PORT_ENDPOINT = 'http://127.0.0.1:8000/json-port/';
  const AGENT_ENDPOINT = 'http://127.0.0.1:8000/json-agent/';

  function getJsonData(endPoint) {
    return new Promise((res, rej) => {
      fetch(endPoint)
        .then(res => res.json())
        .then(result => res(result))
        .catch(err => rej(err))
    });
  }

  const countryList = await getJsonData(COUNTRY_ENDPOINT);
  let portListCash = [];

  const liveSearchElements = document.querySelectorAll('.live-search');
  const countrySelect = document.querySelector('.form-select');
  const portInput = liveSearchElements[0];
  const btnGetAgents = document.getElementById('btn');
  let selectedCountryId = null;
  let prevCountryId = null;

  countryList.forEach(country => {
    optionEl = document.createElement('option');
    optionEl.setAttribute('value', country.id);
    optionEl.innerText = country.name
    countrySelect.appendChild(optionEl);
  })

  countrySelect.addEventListener('change', e => {
    selectedCountryId = countrySelect.value == '0' ? null : countrySelect.value;
    portInput.value = ''
    listEl.innerHTML = ''
  })

  // function liveSearchCountryHandler(searchKey) {
  //   const test = `^${searchKey.trim()}`;
  //   const reg = new RegExp(test, 'i');

  //   if (countryList.length) {
  //     const result = countryList.filter(item => reg.test(item.name));
  //     return Promise.resolve(result);
  //   }
  // }

  function liveSearchPortHandler(searchKey) {
    const countryId = selectedCountryId;
    const test = `^${searchKey.trim()}`;
    const reg = new RegExp(test, 'i');

    if (prevCountryId == countryId && portListCash.length) {
      return Promise.resolve(portListCash.filter(item => reg.test(item.name)))
    }

    if (countryId === null) {
      prevCountryId = countryId;
      return getJsonData(PORT_ENDPOINT)
        .then(portList => {
          portListCash = portList;
          return portList.filter(item => reg.test(item.name));
        })
    }

    prevCountryId = countryId;
    return getJsonData(PORT_ENDPOINT + `${countryId}`)
      .then(portList => {
        portListCash = portList;
        return portList.filter(item => reg.test(item.name));
      })

  }

  const listEl = document.querySelector('.list-group');
  btnGetAgents.addEventListener('click', async () => {
    const port_id = portInput.dataset.value;
    let agent_list = await getJsonData(AGENT_ENDPOINT + `${port_id}`);
    agent_list = agent_list.sort((a, b) => b.appointments - a.appointments)

    let out = '';
    agent_list.forEach(agent => {
      out += `
      <li class="list-group-item d-flex justify-content-between align-items-start">
      <div class="ms-2 me-auto">
        <div class="fw-bold">${agent.name}</div>
        <div>${agent.email}</div>
        <div>${agent.phone}</div>`

      if (agent.website != null)
        out += `<div><a href='https://${agent.website}'>${agent.website}</a></div>`

      out +=`
      </div>
      <span class="badge bg-primary rounded-pill">${agent.appointments}</span>
      </li>`;
    })
    listEl.innerHTML = out;
  })

  new LiveSearchInput(portInput, liveSearchPortHandler);

})();