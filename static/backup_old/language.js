/**
*	language.js
*	Author: Seung Youp Baek
*	Loads language page dynamically
*	4/6/2015
*/

var langId = document.getElementById("param").getAttribute("langId");
//redirect c to c++

var apiPath = "/api/language/" + langId;
var jobApiPath = "/api/job";
var jobJson;

$.ajax({
  url: jobApiPath,
  async: false,
  dataType: 'json',
  success: function (response) {
    jobJson = response;
  }
});

var jobData = jobJson["jobs"];
var jobLen = jobData.length;
var i = 0;
var selectedJson = "";
var cPanel = "<div class=\"panel-group\" id=\"accordion\">";
var jobCounter = 0;

while(i < jobLen){
	var dict = jobData[i];
	var targetId = langId;
	if(langId == 10)
		targetId = 2;	//redirect to c++ 
	if(String(dict["language_ID"]) == String(targetId)){
		selectedJson += ("<p>" + JSON.stringify(dict) + "</p>");
		cPanel += generateCollapsiblePanel(jobCounter, dict["job_title"], dict["link"], dict["company_ID"], dict["location_ID"], dict["job_description"], dict["skillset_ID"]);
		jobCounter++;
	}
	i++;
}

cPanel += "</div>";
document.getElementById("cPanel").innerHTML = cPanel;

jobLen = jobData.length;

$.getJSON(apiPath, function(result){
	var data = result["language"];
	var imgSrc = data["language_image"]; //small
	var description = data["language_wiki_description"];
	var wikiLink = data["language_wiki_link"];

	generateDescription(imgSrc, description, wikiLink);
});

function generateDescription(imageSrc, wikiDescription, wikiLink){	
	var descriptionHtml;
	descriptionHtml = "<div class=\"col-md-4\"><div style='padding-top: 50px';>";
	descriptionHtml += "<img height=\"250\" src=../static/" + imageSrc + " alt=\"Responsive image\" class=\"img-rounded img-response-language\" style='padding-bottom:50px'>";
	descriptionHtml += "<div class=\"panel panel-default\"><div class=\"panel-heading\"><h4 class=\"panel-title\">Description</h4></div><div class=\"panel-body\">";
	descriptionHtml += wikiDescription;
	descriptionHtml += "<br><br>";
	descriptionHtml += "<a href=" + wikiLink + " target=\"_blank\"><button type=\"button\" class=\"btn btn-default\">Read more</button></a>";
	descriptionHtml += "</div></div></div></div>";
	document.getElementById("description").innerHTML=descriptionHtml;
}

function generateCollapsiblePanel(counter, jobName, jobLink, cmpyID, locID, descrip, skillID){
	var returnHTML = "<div class=\"panel panel-default\"><div class=\"panel-heading\"><h4 class=\"panel-title\"><a data-toggle=\"collapse\" data-parent=\"#accordion\" href=\"#collapse" + counter + "\">";
	returnHTML += jobName;
	var inTag = "";
	if(counter == 0)
		inTag = "in";
	returnHTML += "</a></h4></div><div id=\"collapse"+counter+"\" class=\"panel-collapse collapse "+inTag+"\"><div class=\"panel-body\">";

	var companyDict;
	$.ajax({
	  url: "/api/company/" + cmpyID,
	  async: false,
	  dataType: 'json',
	  success: function (response) {
	    // do stuff with response.
	    companyDict = response["company"];
	  }
	});

	var cmpyName = companyDict["company_name"];

	var locDict;
	$.ajax({
	  url: "/api/location/" + locID,
	  async: false,
	  dataType: 'json',
	  success: function (response) {
	    // do stuff with response.
	    locDict = response["location"];
	  }
	});

	var locName = locDict["location_name"];
	// alert("locName = " + locName);
	var locLink = "location/";
	var locSplit = locName.split(',');
	locSplit = locSplit[0].replace(" ", "");
	locSplit = locSplit.toLowerCase();
	locLink += locSplit;

	returnHTML += "<h2><a href=#>"+cmpyName+"</a> <small><a href=../"+locLink+">"+locName+"</a></small></h2>";
	returnHTML += "<hr><h4>Job Description</h4><h5>" + descrip + "</h5>";
	
	var skillDict;
	$.ajax({
	  url: "/api/skillset/" + skillID,
	  async: false,
	  dataType: 'json',
	  success: function (response) {
	    skillDict = response["skillset"];
	  }
	});

	var skillName = skillDict["skillset_name"];
	returnHTML += "<hr><h4>Required Skill(s)</h4><h5><a href=/skillset/"
					+skillName+"><button type=\"button\" class=\"btn btn-default\">"
					+skillName+"</button></a></h5><hr><a href="+jobLink
					+" target=\"_blank\"><button type=\"button\" class=\"btn btn-default\">Show More</button></a></div></div></div>";
	
	return returnHTML;
}
