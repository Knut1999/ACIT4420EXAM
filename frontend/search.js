async function search() {
    const urlGet = "http://localhost:8000/hello";
    const responseGet = await fetch(urlGet);
    const resultGet = await responseGet.json();
    console.log(resultGet);

    //input data from frontend
    const urlPost = "http://localhost:8000/items/";
    const responsePost = await fetch(urlPost, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ destination: document.getElementById("destinations").value , budget: document.getElementById("budget").value}),
    });
    const resultPost = await responsePost.json();
    console.log(resultPost);
}