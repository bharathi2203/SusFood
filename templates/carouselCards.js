var offset = 0;
var endOffset = offset + 4;

var cardsData = [{
    name: "Panera Bread",
    img: "https://www.nrn.com/sites/nrn.com/files/styles/article_featured_retina/public/C222-ChefsChickenSandwiches_H.jpg?itok=jIZV0U7v",
    descrip: "Panera Bread is delicious"
},
{
    name: "Tsaocaa",
    img: "https://avatarfiles.alphacoders.com/121/121594.jpg",
    descrip: "Boba!!"
},
{
    name: "Sorrento Pizzeria & Grill",
    img: "https://media-cdn.tripadvisor.com/media/photo-s/07/64/c5/eb/pizz-traiteur-pizzeria.jpg",
    descrip: "Pizza pizza"
},
{
    name: "Panera Bread2",
    img: "https://www.nrn.com/sites/nrn.com/files/styles/article_featured_retina/public/C222-ChefsChickenSandwiches_H.jpg?itok=jIZV0U7v",
    descrip: "Panera Bread is delicious"
},
{
    name: "Panera Bread3",
    img: "https://www.nrn.com/sites/nrn.com/files/styles/article_featured_retina/public/C222-ChefsChickenSandwiches_H.jpg?itok=jIZV0U7v",
    descrip: "Panera Bread is delicious"
},
{
    name: "Panera Bread4",
    img: "https://www.nrn.com/sites/nrn.com/files/styles/article_featured_retina/public/C222-ChefsChickenSandwiches_H.jpg?itok=jIZV0U7v",
    descrip: "Panera Bread is delicious"
},
{
    name: "Panera Bread5",
    img: "https://www.nrn.com/sites/nrn.com/files/styles/article_featured_retina/public/C222-ChefsChickenSandwiches_H.jpg?itok=jIZV0U7v",
    descrip: "Panera Bread is delicious"
},
{
    name: "Panera Bread6",
    img: "https://www.nrn.com/sites/nrn.com/files/styles/article_featured_retina/public/C222-ChefsChickenSandwiches_H.jpg?itok=jIZV0U7v",
    descrip: "Panera Bread is delicious"
}
]   
getCards()

function getCards (){
    console.log(offset, endOffset)
    if(endOffset > 8){
        endOffset = 4;
        offset = 0;
    }
    else if(offset < 0){
        endOffset = 8;
        offset = 4;
    }

    for(var i = offset; i < endOffset; i++){
        let div = document.createElement('div')
        div.className = "block";
        div.id = i;
        div.innerHTML = `<img src=${cardsData[i].img}}>
            <div class = "name">
                ${cardsData[i].name}
            </div>
            <div class="description">${cardsData[i].descrip}</div>`

        document.getElementById('outputCards').append(div)
    }
}

var leftButton = document.getElementById('leftIcon')
var rightButton = document.getElementById('rightIcon')

leftButton.onclick = function(){
    console.log("clicked!!")
    for(var i = offset; i < endOffset; i ++){
        document.getElementById(i).remove()
    }
    offset -= 4;
    endOffset -=4;
    getCards()
}

rightButton.onclick = function(){
    console.log("clicked!!")
    for(var i = offset; i < endOffset; i ++){
        document.getElementById(i).remove()
    }
    offset += 4; 
    endOffset += 4;
    getCards()
}