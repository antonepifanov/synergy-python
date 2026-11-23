const resultEl = document.getElementById('result');
const plusBtn = document.getElementById('plus');
const minusBtn = document.getElementById('minus');
const messageEl = document.getElementById('message');

let count = 0;

function updateUI() {
    resultEl.textContent = count;
    
    if (count > 0) {
        resultEl.style.backgroundColor = 'yellow';
    } else if (count < 0) {
        resultEl.style.backgroundColor = 'green';
    } else {
        resultEl.style.backgroundColor = 'red';
    }
    
    plusBtn.disabled = count >= 10;
    minusBtn.disabled = count <= -10;
    
    if (count === 10 || count === -10) {
        messageEl.textContent = 'вы достигли экстремального значения';
    } else {
        messageEl.textContent = '';
    }
}

plusBtn.addEventListener('click', () => {
    count++;
    updateUI();
});

minusBtn.addEventListener('click', () => {
    count--;
    updateUI();
});

updateUI();