var langJson;
var cmpyJson;
var locJson;

var state = document.getElementById("navbarParam").getAttribute("state");

$.ajax({
  url: "/api/language",
  async: false,
  dataType: 'json',
  success: function (response) {
    // do stuff with response.
    langJson = response["languages"];
  }
});

$.ajax({
  url: "/api/location",
  async: false,
  dataType: 'json',
  success: function (response) {
    // do stuff with response.
    locJson = response["locations"];
  }
});

$.ajax({
  url: "/api/company",
  async: false,
  dataType: 'json',
  success: function (response) {
    // do stuff with response.
    cmpyJson = response["companies"];
  }
});

var len = langJson.length;

document.getElementById("langMenu").innerHTML = genLangMenu();
document.getElementById("cmpyMenu").innerHTML = genCmpyMenu();
document.getElementById("locMenu").innerHTML = genLocMenu();

function genLangMenu(){
	var i = 0;
	var retHTML = "";
	var linkPrefix = "";
	if(state == 0)
		linkPrefix += "language/";

	for(i = 0; i<len; i++){
		var dict = langJson[i];
		var langName = dict["language_name"];
		var langAddr = langName.replace(" ", "");
		retHTML += "<li><a href="+linkPrefix+langAddr+">"+langName+"</a></li>"
	}
	return retHTML;
}

function genCmpyMenu(){
	var i = 0;
	var retHTML = "";
	var linkPrefix = "";
	if(state == 0)
		linkPrefix += "company/";

	for(i = 0; i<len; i++){
		var dict = cmpyJson[i];
		var cmpyName = dict["company_name"];
		var cmpyAddr = cmpyName.replace(" ", "");
		retHTML += "<li><a href="+linkPrefix+cmpyAddr+">"+cmpyName+"</a></li>"
	}
	return retHTML;
}

function genLocMenu(){
	var i = 0;
	var retHTML = "";
	var linkPrefix = "";
	if(state == 0)
		linkPrefix += "location/";

	for(i = 0; i<len; i++){
		var dict = locJson[i];
		var locName = dict["location_name"];
		var locAddr = locName.replace(" ", "");
		locAddr = locAddr.replace(",", "");
		retHTML += "<li><a href="+linkPrefix+locAddr+">"+locName+"</a></li>"
	}
	return retHTML;
}