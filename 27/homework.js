// Task 1
const myDiv = document.createElement('div');
myDiv.className = "buttons";

['Add to friends', 'Send message', 'Offer a job'].map(buttonname => {
    let button = document.createElement('button');
    button.className = 'btn btn-success';
    button.innerText = `${buttonname}`;
    button.style.margin = '15px';
    myDiv.appendChild(button);
})

document.getElementsByTagName('p')[0].appendChild(myDiv);

// Task 2
const myDiv1 = document.createElement('div');
myDiv1.className = "buttons";

let button1 = document.createElement('button');
button1.className = 'btn btn-success';
button1.style.margin = '15px';
myDiv1.appendChild(button1);

document.getElementsByTagName('p')[0].appendChild(myDiv1);

const btn4 = document.getElementsByTagName('button')[3];
let i = Math.floor(Math.random() * (1000));
window.onload = () => btn4.innerText = `Number of friends: ${i}`;

const btn1 = document.getElementsByTagName('button')[0];
btn1.onclick = () => btn4.innerText = `Number of friends: ${++i}`;

// Task 3
btn1.addEventListener('click', () => {
    btn1.disabled = true;
    btn1.innerText = 'Confirmation is pending'
})

// Task 4
const btn2 = document.getElementsByTagName('button')[1];
btn2.onclick = () => btn2.style.background === 'salmon' ? btn2.style.background = '#198754': btn2.style.background = 'salmon';

// Task 5
const btn3 = document.getElementsByTagName('button')[2];
btn3.onclick = () => btn1.style.visibility === 'hidden' ? btn1.style.visibility = 'visible' : btn1.style.visibility = 'hidden';

//Task 6
let button2 = document.createElement('button');
button2.className = 'btn btn-success';
button2.innerText = 'Submit the homework';
button2.style.margin = '15px';

document.getElementsByTagName('div')[1].appendChild(button2);

const btn5 = document.getElementsByTagName('button')[4];
btn5.onclick = () => {
    let newRow = document.createElement('tr')
    let newEntry1 = document.createElement('td')
    let newEntry2 = document.createElement('td')
    let newEntry3 = document.createElement('td')
    newEntry1.innerText = prompt("Please enter lesson number:")
    newEntry2.innerText = prompt("Please enter lesson name:")
    newEntry3.innerText = prompt("Please enter homework grade:")
    newRow.append(newEntry1, newEntry2, newEntry3)
    document.getElementsByTagName('tbody')[0].appendChild(newRow)
}