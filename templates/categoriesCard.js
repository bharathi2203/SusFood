var offset2 = 0;
var endoffset2 = offset2 + 4;

var foodCategories = [
    { cuisine: "Breakfast", img: "pics/sunSide.png"}, 
    { cuisine: 'Chinese', img: "pics/dumplings.png"} , 
    { cuisine: 'Seafood', img: "pics/crab.png"} ,
    { cuisine: 'Mexican', img: "pics/taco.png"}, 
    { cuisine: 'Vegetarian', img: "pics/broccoli.png"} , 
    { cuisine: 'Japanese', img : "pics/sushi.png"},
    { cuisine: 'Dessert', img: "pics/strawberryCheese.png"},
    { cuisine: 'Indian', img: "pics/pepper.png"}]   

getCardz()

function getCardz (){
    console.log(offset2, endoffset2)
    if(endoffset2 > 8){
        endoffset2 = 4;
        offset2 = 0;
    }
    else if(offset2 < 0){
        endoffset2 = 8;
        offset2 = 4;
    }

    for(var i = offset2; i < endoffset2; i++){
        let div = document.createElement('div')
        div.className = "categoryContainer";
        div.id = "food" + String(i);
        div.innerHTML = 
        `<img class = foodIconImg src="${foodCategories[i].img}">
            <div class = "cuisine">
                ${foodCategories[i].cuisine}
            </div>`

        document.getElementById('foodCategories').append(div)
    }
}

var leftButton2 = document.getElementById('leftIcon2')
var rightButton2 = document.getElementById('rightIcon2')

leftButton2.onclick = function(){
    for(var i = offset2; i < endoffset2; i ++){
        document.getElementById("food".concat(String(i))).remove()
    }
    offset2 -= 4;
    endoffset2 -=4;
    getCardz()
}

rightButton2.onclick = function(){
    for(var i = offset2; i < endoffset2; i ++){
        document.getElementById("food".concat(String(i))).remove()
    }
    offset2 += 4; 
    endoffset2 += 4;
    getCardz()
}