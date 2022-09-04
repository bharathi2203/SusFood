import distanceData from "../data/DataSet1.json" assert {type: "json"}

getDistanceMetrics()

// 5 star: 0-300m
// 4 star: 300-500
// 3 star: 500-700
// 2 star: 700-900
// 1 star: 900+

function getTier(distance){
    if(distance <= 299){
        return '<span class="fa fa-leaf checked"></span><span class="fa fa-leaf checked"></span><span class="fa fa-leaf checked"></span><span class="fa fa-leaf checked"></span><span class="fa fa-leaf checked"></span>';
    }
    else if((300 <= distance) && (distance <= 499)){
        return '<span class="fa fa-leaf checked"></span><span class="fa fa-leaf checked"></span><span class="fa fa-leaf checked"></span><span class="fa fa-leaf checked"></span><span class="fa fa-leaf"></span>';
    }
    else if((500 <= distance) && (distance <= 699)){
        return '<span class="fa fa-leaf checked"></span><span class="fa fa-leaf checked"></span><span class="fa fa-leaf checked"></span><span class="fa fa-leaf"></span><span class="fa fa-leaf"></span>';
    }
    else if((700 <= distance) && (distance <= 899)){
        return '<span class="fa fa-leaf checked"></span><span class="fa fa-leaf checked"></span><span class="fa fa-leaf"></span><span class="fa fa-leaf"></span><span class="fa fa-leaf"></span>'; 
    }
    else if((900 <= distance) && (distance <= 999)){
        return '<span class="fa fa-leaf checked"></span><span class="fa fa-leaf"></span><span class="fa fa-leaf"></span><span class="fa fa-leaf"></span><span class="fa fa-leaf"></span>';
    }
    else{
        return '<span class="fa fa-leaf"></span><span class="fa fa-leaf"></span><span class="fa fa-leaf"></span><span class="fa fa-leaf"></span><span class="fa fa-leaf"></span>';
    }
}

function getDistance(distance){
    return '<div id="distance">${distance}</div>';
}

function getDistanceMetrics (){
    let div = document.createElement('div');
    div.className = "sus-metric";
    div.id = "distance-rating";
    div.innerHTML = getTier(distanceData.distance);
    document.getElementById('distanceContainer').append(div);

    let div2 = document.createElement('div2');
    div.className = "metric";
    div.id = "distance";
    div.innerHTML = getDistance(distanceData.distance);
    document.getElementById('metricContainer').append(div2);
}