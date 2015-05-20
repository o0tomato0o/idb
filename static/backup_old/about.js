/**
*	about.js
*	Author: Seung Youp Baek
*	Loads about page dynamically
*	4/6/2015
*/

var aboutJson;

$.ajax({
	url: "/api/member",
	async: false,
	dataType: 'json',
	success: function (response) {
	aboutJson = response["members"];
	}
});

var len = aboutJson.length;
var i = 0;
var leaderHTML = "<div class=\"col-md-12\"><hr><div align = \"center\"><h2>Group Leaders</h2><h3>";
var memberHTML = "";
var head = "<div class=\"row row-format\" align=\"center\"><div class=\"col-md-2 col-md-offset-3\">";
var foot = "</div></div></div><hr>";
var leaderCount = 1;
var totalCommit = 0;
var totalIssue = 0;
var totalUnittest = 0;
var teamStatHTML = "";

for(i = 0; i<len; i++){
	// alert("yay");
	var data = aboutJson[i];
	var imgSrc = data["member_image"];
	var memName = data["member_name"];
	var memBio = data["member_bio"];
	var memRespon = data["member_major_responsibility"];
	var memCommit = data["member_commit"];
	var memIssue = data["member_issue"];
	var memUnittest = data["member_unittest"];
	memberHTML += head;
	memberHTML += "<img src=\""+imgSrc+"\" alt=\"Responsive image\" class=\"img-rounded img-response-profile\"></div><div class=\"col-md-4 col-md-offset-2\"><div align=\"left\">";
	memberHTML += "<h1><b/>" + memName + "</h1><br><h4><b/>Bio<br></h4><h5>" + memBio + "</h5><h4><b/>Major Responsibilities<br></h4><h5>" + memRespon + "</h5><h4/><b/>Stats<h5/>" + memCommit + " commit(s)<h5/>" + memIssue + " issue(s)<br><h5/>" + memUnittest + " unittest(s)<br>";
    memberHTML += foot;

    totalCommit += memCommit;
    totalIssue += memIssue;
    totalUnittest += memUnittest;

    var isLeader = data["member_leader"];
    if(isLeader){
    	leaderHTML += leaderCount + ". " + memName + "<br><br>";
    	leaderCount++;
    }
}
leaderHTML += "</h3></div><BR><BR><BR><hr><br></div>";
document.getElementById("leaders").innerHTML = leaderHTML;
document.getElementById("members").innerHTML = memberHTML;

teamStatHTML += "<h3/><b/>Total Stats<h5/>"+totalCommit+" Commits<br>"+totalIssue+" Issues<br>"+totalUnittest+" Unittests";
document.getElementById("teamStat").innerHTML = teamStatHTML;