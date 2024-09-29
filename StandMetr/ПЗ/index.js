document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('myForm');
    var submitBtn = document.getElementById('submitBtn');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var height = document.getElementById('height').value;
        var weight = document.getElementById('weight').value;
        var goal = document.getElementById('goal').value;

        var ration = calculateRation(height, weight, goal);

        document.getElementById('rationResult').innerHTML = ration;
    });
});

function calculateRation(height, weight, goal) {
    console.log(height, weight, goal);
    var ration = [];
    var bmi = weight / ((height / 100) ** 2);
    var totalCalories = 0;

    if (goal === 'lose_weight') {
        if (bmi < 18.5) {
            return 'Ви занадто худі, щоб схуднути. Вам потрібно набрати вагу.';
        } else {
            while (totalCalories < 2500) {
                ration = generateRation();
                totalCalories = calculateTotalCalories(ration);
            }
        }
    } else if (goal === 'gain_weight') {
        if (bmi > 25) {
            return 'Ви занадто повні, щоб набирати вагу. Вам потрібно скинути зайву вагу.';
        } else {
            while (totalCalories < 3000) {
                ration = generateRation();
                totalCalories = calculateTotalCalories(ration);
            }
        }
    }

    var rationStr = '';
    ration.forEach(function(meal) {
        rationStr += '<strong>' + meal.meal + ':</strong><br>';
        meal.foods.forEach(function(food) {
            rationStr += '- ' + food.name + ' (' + food.calories + ' ккал)<br>';
        });
        rationStr += '<br>';
    });
    return rationStr;
}

// Генерация рациона
function generateRation() {
    var breakfastOptions = [
        { name: 'Вівсянка', calories: 300 },
        { name: 'Яйця з овочами', calories: 350 },
        { name: 'Гречка з йогуртом', calories: 400 }
    ];
    var lunchOptions = [
        { name: 'Куряча грудка з овочами', calories: 450 },
        { name: 'Рис з тушеними овочами', calories: 400 },
        { name: 'Салат з тунцем та оливковою олією', calories: 350 }
    ];
    var dinnerOptions = [
        { name: 'Творог з фруктами', calories: 250 },
        { name: 'Риба з овочами', calories: 300 },
        { name: 'Квасоля з овочами та горіхами', calories: 350 }
    ];

    var ration = [
        { meal: 'Сніданок', foods: getRandomSubset(breakfastOptions) },
        { meal: 'Обід', foods: getRandomSubset(lunchOptions) },
        { meal: 'Вечеря', foods: getRandomSubset(dinnerOptions) }
    ];

    return ration;
}

// Вычисление общего количества калорий в рационе
function calculateTotalCalories(ration) {
    var totalCalories = 0;
    ration.forEach(function(meal) {
        meal.foods.forEach(function(food) {
            totalCalories += food.calories;
        });
    });
    return totalCalories;
}

// Получение случайного подмножества из массива
function getRandomSubset(array) {
    var shuffledArray = array.slice().sort(() => Math.random() - 0.5);
    return shuffledArray.slice(0, Math.floor(Math.random() * shuffledArray.length) + 1);
}
