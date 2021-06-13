function copyURI(evt) {
    evt.preventDefault();
    navigator.clipboard.writeText("http://127.0.0.1:8000"+evt.target.getAttribute('href')).then(() => {

    }, () => {
      /* clipboard write failed */
    });
}

function copyURI2(evt) {
    evt.preventDefault();
    navigator.clipboard.writeText(evt.target.previousSibling.textContent).then();
}

var exampleEl = document.getElementById('myBtn')
var popover = new bootstrap.Popover(document.querySelector('.example-popover'), {
  container: 'body'
})