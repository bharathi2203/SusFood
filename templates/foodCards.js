const layout = document.createElement('layout');
layout.innerHTML = `
<style> 
    .block {
        display: inline-block;
        width: 250px;
        height: 300px;
        background-color: #f8f6ee;
        border-radius: 30px;
        margin-right: 2.5%;
    }
    .name{
        font-family: 'Gaegu', cursive;
        font-size: 22px;
        font-weight: bold;
        margin-top: 3%;
        text-align: center;
    }
    .description{
        margin-top: 0;
        margin-left: 10%;
        font-family: 'Lato', sans-serif;
        font-size: 15px;
        color: grey;
        text-align: left;
    }
<\style>
`


class foodCards extends HTMLElement {
    


    constructor(){
        super();
        this.innerHTML = `${this.getAttribute('restName')}`;
        this.shadowRoot.appendChild(layout.content.cloneNode(true));
    }
}

window.customElements.define('food-card', foodCards);