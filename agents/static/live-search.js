class LiveSearchInput {
  constructor(inputEl, fnCall) {
    this.__inputEl = inputEl;
    this.__liveSearchWindow = document.createElement('div');
    this.getResult = fnCall;
    this.__init();
  }

  __init() {
    this.__liveSearchWindow.classList.add('live-search__window');
    this.__inputEl.parentElement.insertBefore(this.__liveSearchWindow, this.__inputEl.nextSubling);

    this.__inputEl.addEventListener('input', async (e) => {
      const searchResult = await this.getResult(e.target.value);
      console.log(searchResult)
      let out = '';
      searchResult.forEach(item => {
        out += `<div class="live-search__item" data-value=${item.id}>${item.name}</div>`
      })
      this.__liveSearchWindow.innerHTML = out;
      this.__liveSearchWindow.classList.add('live-search__window--active');
    })

    this.__inputEl.addEventListener('blur', (e) => {
      setTimeout(() => {
        this.__liveSearchWindow.classList.remove('live-search__window--active');
      }, 150)
    })

    this.__liveSearchWindow.addEventListener('click', (e) => {
      this.__inputEl.value = e.target.innerText;
      this.__inputEl.dataset.value = e.target.dataset.value;
    })
  }

}