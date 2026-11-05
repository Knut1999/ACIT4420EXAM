function moveSliders(){
    
    const type = document.getElementById("budgetType").value;

    if (type == "Budget traveller") {
        document.getElementById("priceWeight").value = 80;
        document.getElementById("durationWeight").value = 10;
        document.getElementById("timeWeight").value = 30;
        document.getElementById("flexibilityWeight").value = 10;
        document.getElementById("ratingWeight").value = 10;
        document.getElementById("transfersWeight").value = 10;
        document.getElementById("environmentWeight").value = 5;
    }

    else if (type == "Business traveller") {
        document.getElementById("priceWeight").value = 10;
        document.getElementById("durationWeight").value = 80;
        document.getElementById("timeWeight").value = 80;
        document.getElementById("flexibilityWeight").value = 30;
        document.getElementById("ratingWeight").value = 60;
        document.getElementById("transfersWeight").value = 70;
        document.getElementById("environmentWeight").value = 5;
    }

    else if (type == "Flexibility-focused tourist") {
        document.getElementById("priceWeight").value = 20;
        document.getElementById("durationWeight").value = 20;
        document.getElementById("timeWeight").value = 20;
        document.getElementById("flexibilityWeight").value = 100;
        document.getElementById("ratingWeight").value = 60;
        document.getElementById("transfersWeight").value = 30;
        document.getElementById("environmentWeight").value = 10;
    }

    else if (type == "Environment-focused traveller") {
        document.getElementById("priceWeight").value = 10;
        document.getElementById("durationWeight").value = 10;
        document.getElementById("timeWeight").value = 10;
        document.getElementById("flexibilityWeight").value = 10;
        document.getElementById("ratingWeight").value = 20;
        document.getElementById("transfersWeight").value = 20;
        document.getElementById("environmentWeight").value = 100;
    }
}