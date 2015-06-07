"use strict";

angular.module("signal_app", ["ngRoute", "signal_app.hello"])
    .config(["$routeProvider", function($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/menu'});
    }])
    .controller("MainCtrl", ["$scope", "$route", "$location",
            function($scope, $route, $location) {
                //console.log($route);
                //console.log($location.path());
    }]);

