console.log("Javascript fully loaded properly");

/**
*	Description: Contain the main functionality of the entire project in JS code through the use of Angular JS
*		Angular JS lets us have the ability to shift our Server Side functionality to the Front End
*		So long as we keep the sensitive information on the server, and not here, this is perfectly acceptable
*
*	File: 					MyScript.js
*	Author: 				Wesley Couturier
*	Date (last modified): 	11-7-2016 (mm-dd-yyyy)
*/

// The ONLY globals we will have.
var app = angular.module("myApp", []);

// Service contains variables and functions that multiple controllers might need access to.
// You can only get access to service variables through the use of it's functions, a.k.a. Encapsulation.
app.service('activeTabs', function() {
	// IDs for the tabs that determine which tab is active, so we know where to post our tab content
	var myIDs = {
		"people": angular.element(document.querySelector('#People')),
		"places": angular.element(document.querySelector('#Places')),
		"purpose": angular.element(document.querySelector('#Purpose'))
	};

	// Bool to double check if we're allowed to get new content
	var reload = true;

	// Set/Dictionary used to contain the current contents of each tab. Why make another query when we had
	// it before?
	var myJobs = {
		"programming": "",
		"writing": "",
		"all": ""
	};

	return {
		// Returns specified set/Dictionary
		getJobBoard: function(idToGet) {
			var temp = Object.keys(myJobs);
			for (var i = 0; i < temp.length; i++) {
				if (angular.equals(temp[i], idToGet)) {
					return myJobs[temp[i]];
				}
			}
		},
		// Sets specified set/Dictionary in the Service
		setJobBoard: function(idToChange, myJson) {
			var temp = Object.keys(myJobs);
			for (var i = 0; i < temp.length; i++) {
				if (angular.equals(temp[i], idToChange)) {
					myJobs[temp[i]] = myJson;
				}
			}
		},

		getReload: function() {
			return reload;
		},

		setReload: function(boolIn) {
			reload = boolIn;
		},

		getIDs: function() {
			return myIDs;
		},
		// If we want to know which tab we're on, we need to check which one is active. This function
		// updates our service IDs so we know which one is active.
		updateIDs: function() {
			myIDs = {
				"programming": angular.element(document.getElementById('ProgrammingJobs')),
				"writing": angular.element(document.getElementById('WritingJobs')),
				"all": angular.element(document.getElementById('AllJobs'))
			};
		},

		reloadContainer: function() {
			// Need to make sure we get the right info for the right tab
			this.updateIDs();
			// tell parseString to remake url and Query
			reload = true;
			return this.getJobBoard();
		}
	};
});

// Parent Controller used to take broadcast event and data from one child to another
app.controller("tabParent", function($scope, activeTabs, $sce) {
    // Nothing for right now
});

// Controller used to broadcast to sibling controller to update tab content
app.controller("myCtrl", function($scope, $http, activeTabs) {
	$scope.getUpdate = function($event) {
		// This will call the "url_reload_check_two" function in Parent to give this controller's
		// sibling the tab we seleted.
		$scope.$parent.$broadcast("url_reload_check_two", $event.target.hash);
	};
});

// Controller that handles the tab content, url building and querying from Indeed's API
app.controller("parseString", function($scope, $sce, $http, activeTabs) {
	// NEED variable of this instance. You'll see later.
	var vm = this;
	// Which tab ID is Active for tab content load.
	var currentId = "";
	// Empty container for response returns.
	vm.response = [];

	// Some defaults to get the ball rolling.
	$scope.indeedStringBuild["q"] = "People";
	currentId = "People";
});
