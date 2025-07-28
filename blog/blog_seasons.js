function seasons(date = new Date()) {
    const month = date.getMonth();
    const day = date.getDate();

    if (month >= 2 && month <= 4) {if (month === 3 && day === 30) {return "Reunification Day"} return "Spring";}
    else if (month >= 5 && month <= 7) {return "Summer";}
    else if (month >= 8 && month <= 10) {if (month === 8) {if (day === 2) {return "Independence Day";} else if (day === 15) {return "My birthday!";}} return "Autumn";}
    else {if (month === 0 && day === 1 || month === 11 && day === 31) {return "New Year's Day"}} {return "Winter";}
}

const today = new Date();
const currentSeason = seasons(today);
console.log(currentSeason)
if (currentSeason === "Spring" || currentSeason === "Reunification Day") {
    document.getElementById("season").textContent = "body {background-image: url('https://upload.wikimedia.org/wikipedia/commons/f/fb/XN_Fruehjahrswiese_00.jpg');}";
    document.getElementById("credit").innerText = "Credit for the background: Original: Guido Gerding / Wikimedia Commons / “XN Fruehjahrswiese 00” / CC BY-SA 3.0";
    } // Original: Guido Gerding / Wikimedia Commons / “XN Fruehjahrswiese 00” / CC BY-SA 3.0
else if (currentSeason === "Summer") {
    document.getElementById("season").textContent = "body {background-image: url('https://upload.wikimedia.org/wikipedia/commons/c/c4/Field_Hamois_Belgium_Luc_Viatour.jpg');}";
    document.getElementById("credit").innerText = "Credit for the background: Original: Luc Viatour | https://Lucnix.be / Wikimedia Commons / “Field Hamois Belgium Luc Viatour” / CC BY-SA 3.0";
    } // Original: Luc Viatour | https://Lucnix.be / Wikimedia Commons / “Field Hamois Belgium Luc Viatour” / CC BY-SA 3.0
else if (currentSeason === "Autumn" || currentSeason === "Independence Day" || currentSeason === "My birthday!") {
    document.getElementById("season").textContent = "body {background-image: url('https://upload.wikimedia.org/wikipedia/commons/d/d0/D%C3%BClmen%2C_Wildpark_--_2014_--_3808_color_balanced.jpg');}";
    document.getElementById("credit").innerText = "Credit for the background: Original: Dietmar Rabich (Derivative work: Sting) / Wikimedia Commons / “Dülmen, Wildpark -- 2014 -- 3808 color balanced” / CC BY-SA 4.0;"
    } // Original: Dietmar Rabich (Derivative work: Sting) / Wikimedia Commons / “Dülmen, Wildpark -- 2014 -- 3808 color balanced” / CC BY-SA 4.0
else {
    document.getElementById("season").textContent = "body {background-image: url('https://upload.wikimedia.org/wikipedia/commons/b/b0/Winter_forest_silver.jpg');}";
    document.getElementById("credit").innerText = "Credit for the background: Original: Ernst Vikne / Wikipedia Commons / “Winter forest silver” / CC BY-SA 2.0";
    } // Original: Ernst Vikne / Wikipedia Commons / “Winter forest silver” / CC BY-SA 2.0
