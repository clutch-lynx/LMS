const form = document.getElementById('name-form');
const nameValue = document.getElementById('name-value')
form.addEventListener('submit', function (e) {
    e.preventDefault(); 
    const formData = new FormData(form)
    fetch("", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        nameValue.textContent = data.name; 
    });
});