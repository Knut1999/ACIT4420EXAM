
var myArray = [
    {'Rank':'bedrift1', 'Company':'Vy','Price':'128$' ,'Depature':'11:23', 'Arrival':'11:23'},
    {'Rank':'bedrift1', 'Company':'Vyy','Price':'128$' ,'Depature':'11:23', 'Arrival':'11:23'},
    {'Rank':'bedrift1', 'Company':'Vy','Price':'128$' ,'Depature':'11:23', 'Arrival':'11:23'},
    {'Rank':'bedrift1', 'Company':'Vy','Price':'128$' ,'Depature':'11:23', 'Arrival':'11:23'},
]

buildTable(myArray)



function buildTable(data){
    var table = document.getElementById('myTable')

    for (var i = 0; i < data.length; i++){
        var row = `<tr>
                        <td>${data[i].Rank}</td>
                        <td>${data[i].Company}</td>
                        <td>${data[i].Price}</td>
                        <td>${data[i].Depature}</td>
                        <td>${data[i].Arrival}</td>
                    </tr>`
        table.innerHTML += row
    }
}
