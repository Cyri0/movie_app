console.log("JS works!");

const MOVIES_API = "/api/movies/"

let wrapper = document.getElementById("wrapper")

fetch(MOVIES_API)
.then(res => res.json())
.then(data => {
    data.forEach(movie => {
        wrapper.appendChild(generateCard(movie))
    });
})

function generateCard(movie){
    let card = document.createElement('div')
    card.classList.add('card')

    // KÉP
    let img = document.createElement('img')
    img.src = movie.poster_image
    card.appendChild(img)

    // CÍM
    let title = document.createElement('h2')
    title.innerText = movie.title
    card.appendChild(title)
    
    // RATING
    let rating_text = document.createElement('h3')
    rating_text.innerHTML = `${movie.average_rating}<span>/5</span>`
    card.appendChild(rating_text)

    return card
}