function copyURI(evt) {
    evt.preventDefault();
    navigator.clipboard.writeText("http://127.0.0.1:8000"+evt.target.getAttribute('href')).then(() => {

    }, () => {
      /* clipboard write failed */
    });
}