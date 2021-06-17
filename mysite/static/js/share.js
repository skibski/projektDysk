function copyURI(evt) {
    evt.preventDefault();
    navigator.clipboard.writeText("http://142.93.105.213"+evt.target.getAttribute('href')).then(() => {

    }, () => {
      /* clipboard write failed */
    });
}

function copyURI2(evt) {
    evt.preventDefault();
    navigator.clipboard.writeText(evt.target.previousSibling.textContent).then();
}

