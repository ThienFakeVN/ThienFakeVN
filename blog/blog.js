function specialDate(date = new Date()) {
    const month = date.getMonth();
    const day = date.getDate();

    if (month >= 2 && month <= 4) {if (month === 3 && day === 30) {return "Reunification Day"} return "Spring";}
    else if (month >= 5 && month <= 7) {return "Summer";}
    else if (month >= 8 && month <= 10) {if (month === 8) {if (day === 2) {return "Independence Day";} else if (day === 15) {return "My birthday!";}} return "Autumn";}
    else {if (month === 0 && day === 1 || month === 11 && day === 31) {return "New Year's Day"}} {return "Winter";}
}

/*const today = new Date();
let background;
if today == specialDate(today): background = */
