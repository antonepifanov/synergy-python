const num1El = document.getElementById('num1');
const num2El = document.getElementById('num2');
const resultEl = document.getElementById('result');

// Функции операций
function sum(a, b) {
   return a + b;
}

function diff(a, b) {
   return a - b;
}

function mult(a, b) {
   return a * b;
}

function div(a, b) {
   if (b === 0) {
      throw new Error('Деление на ноль невозможно');
   }
   return a / b;
}

// Общая функция вычисления
function calculate(operation) {
   const raw1 = num1El.value.trim();
   const raw2 = num2El.value.trim();
   
   if (raw1 === '' || raw2 === '') {
      showError('Введите оба числа');
      return;
   }

   const a = Number(raw1);
   const b = Number(raw2);

   if (!Number.isFinite(a) || !Number.isFinite(b)) {
      showError('Введите корректные числа');
      return;
   }

   try {
      const result = operation(a, b);
      showResult(result);
   } catch (e) {
      showError(e.message);
   }
}

function showResult(value) {
   resultEl.textContent = value;
   resultEl.classList.remove('error');
}

function showError(message) {
   resultEl.textContent = message;
   resultEl.classList.add('error');
}

// Обработчики событи
document.getElementById('btn-sum').addEventListener('click', () => {
   calculate(sum);
});

document.getElementById('btn-diff').addEventListener('click', () => {
    calculate(diff);
});

document.getElementById('btn-mult').addEventListener('click', () => {
   calculate(mult);
});

document.getElementById('btn-div').addEventListener('click', () => {
   calculate(div);
});