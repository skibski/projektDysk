function copyURI(evt) {
    evt.preventDefault();
    navigator.clipboard.writeText("http://165.227.165.148"+evt.target.getAttribute('href')).then(() => {

    }, () => {
      /* clipboard write failed */
    });
}

function copyURI2(evt) {
    evt.preventDefault();
    navigator.clipboard.writeText(evt.target.previousSibling.textContent).then();
}
