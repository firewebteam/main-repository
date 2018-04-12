var blueAmount = document.getElementById("blueCash");
var greenAmount = document.getElementById("greenCash");
var yellowAmount = document.getElementById("yellowCash");

var blue = document.getElementById("blueAuction");
var green = document.getElementById("greenAuction");
var yellow = document.getElementById("yellowAuction");

var pot = document.getElementById("pot");

var blueMoney = 5000;
var greenMoney = 5000;
var yellowMoney = 5000;

var blueCurrentMoney = 0;
var greenCurrentMoney = 0;
var yellowCurrentMoney = 0;

var potValue = 0;

var startingCash = 200;

window.addEventListener('keydown', function (event) {

	console.log(event.keyCode);

	switch (event.keyCode) {

		case 78: //Przycisk 'n' - start gry, zabranie po 200$ każdej drużynie

			blueMoney -= startingCash;
			greenMoney -= startingCash;
			yellowMoney -= startingCash;

			blueCurrentMoney += startingCash;
			greenCurrentMoney += startingCash;
			yellowCurrentMoney += startingCash;


			blue.textContent = blueCurrentMoney;
			yellow.textContent = yellowCurrentMoney;
			green.textContent = greenCurrentMoney;

			yellowAmount.textContent = yellowMoney;
			greenAmount.textContent = greenMoney;
			blueAmount.textContent = blueMoney;

			potValue = potValue + blueCurrentMoney + greenCurrentMoney + yellowCurrentMoney;

			pot.textContent = potValue;
			break;

		case 65: // Przycisk 'a' - dodanie 100$ do licytacji niebieskich
			blueMoney -= 100;
			blueAmount.textContent = blueMoney;
			blueCurrentMoney += 100;
			blue.textContent = blueCurrentMoney;
			potValue += 100;
			pot.textContent = potValue;
			break;

		case 83: // Przycisk 's' - dodanie 100$ do licytacji zielonych
			greenMoney -= 100;
			greenAmount.textContent = greenMoney;
			greenCurrentMoney += 100;
			green.textContent = greenCurrentMoney;
			potValue += 100;
			pot.textContent = potValue;
			break;

		case 68:
			yellowMoney -= 100; // Przycisk 'd' - dodanie 100$ do licytacji żółtych
			yellowAmount.textContent = yellowMoney;
			yellowCurrentMoney += 100;
			yellow.textContent = yellowCurrentMoney;
			potValue += 100;
			pot.textContent = potValue;
			break;

		case 81: // Przycisk 'q' - odjęcie 100$ od licytacji niebieskich
			blueMoney += 100;
			blueAmount.textContent = blueMoney;
			blueCurrentMoney -= 100;
			blue.textContent = blueCurrentMoney;
			potValue -= 100;
			pot.textContent = potValue;
			break;

		case 87: // Przycisk 'w' - odjęcie 100$ od licytacji zielonych
			greenMoney += 100;
			greenAmount.textContent = greenMoney;
			greenCurrentMoney -= 100;
			green.textContent = greenCurrentMoney;
			potValue -= 100;
			pot.textContent = potValue;
			break;

		case 69: // Przycisk 'e' - odjęcie 100$ od licytacji żółtych
			yellowMoney += 100;
			yellowAmount.textContent = yellowMoney;
			yellowCurrentMoney -= 100;
			yellow.textContent = yellowCurrentMoney;
			potValue -= 100;
			pot.textContent = potValue;
			break;

		case 90: // Przycisk 'z' - vabank niebieskich
			potValue += blueMoney;
			pot.textContent = potValue;
			blueCurrentMoney = blueMoney + blueCurrentMoney;
			blue.textContent = blueCurrentMoney;
			blueMoney = blueMoney - blueMoney;
			blueAmount.textContent = blueMoney;
			break;

		case 88: // Przycisk 'x' - vabank zielonych
			potValue += greenMoney;
			pot.textContent = potValue;
			greenCurrentMoney = greenMoney + greenCurrentMoney;
			green.textContent = greenCurrentMoney;
			greenMoney = greenMoney - greenMoney;
			greenAmount.textContent = greenMoney;
			break;

		case 67: // Przycisk 'c' - vabank żółtych
			potValue += yellowMoney;
			pot.textContent = potValue;
			yellowCurrentMoney = yellowMoney + yellowCurrentMoney;
			yellow.textContent = yellowCurrentMoney;
			yellowMoney = yellowMoney - yellowMoney;
			yellowAmount.textContent = yellowMoney;
			break;

		case 80: // Przycisk 'p' - zerowanie licytacji
			yellowCurrentMoney = 0;
			greenCurrentMoney = 0;
			blueCurrentMoney = 0;
			blue.textContent = blueCurrentMoney;
			green.textContent = greenCurrentMoney;
			yellow.textContent = yellowCurrentMoney;

			break;

		case 74: // Przycisk 'j' - przyznanie puli niebieskim
			blueMoney += potValue;
			blueAmount.textContent = blueMoney;
			potValue = 0;
			pot.textContent = potValue;
			break;

		case 75: // Przycisk 'k' - przyznanie puli zielonym
			greenMoney += potValue;
			greenAmount.textContent = greenMoney;
			potValue = 0;
			pot.textContent = potValue;
			break;

		case 76: // Przycisk 'l' - przyznanie puli żółtym
			yellowMoney += potValue;
			yellowAmount.textContent = yellowMoney;
			potValue = 0;
			pot.textContent = potValue;
			break;
	}

}, false);
