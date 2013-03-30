// V 0.0018
$APIKey = "e03537e53f376e69c7e33c0ea6970529";
$businessID = "904965";
$listingID = "899892";

fullstarimagelocation = '/static/images/star.gif';
halfstarimagelocation = '/static/images/halfstar.gif';
url = "http://api.n49.ca/API/rest/JSON?api_key=" + $APIKey + "&action=Reviews.getAllReviews&callback=?";
reviewuslink = "http://www.n49.ca/d/" + $listingID + "?review_me=1";
usesamples = 0;


var m_names = new Array("Jan", "Feb", "Mar","Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec");


var jQueryScriptOutputted = false;

function initJQuery() {
    if (typeof(jQuery) == 'undefined') {
        if (!jQueryScriptOutputted) {
            jQueryScriptOutputted = true;
            document.write("<scr" + "ipt type=\"text/javascript\" src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js\"></scr" + "ipt>");
			if (window.location.hash == "#sample"){
				usesamples = 1;
				document.write("<scr" + "ipt type=\"text/javascript\" src=\"js/samplereviews.js\"></scr" + "ipt>");
			} else if (window.location.hash == "#sample30") {
				usesamples = 1;
				document.write("<scr" + "ipt type=\"text/javascript\" src=\"js/30samplereviews.js\"></scr" + "ipt>");
			}
        }
        setTimeout("initJQuery()", 50);
    } else {
        $(function() {
			texttobereplaced = '';
			$("a[href='http://www.n49.ca/d/listingid']").attr('href', 'http://www.n49.ca/d/' + $listingID);
			
			if (usesamples === 0) {
				$.getJSON(url , function(data) {
					processData(data);
				});
			} else {
				processData(data);
			}
        });
    }
}

function processData(data){
 jQuery.each(data.reviews.review, function(i, val) {
					reviewsCount++;
                    id = val.id;
                    rating = parseFloat(val.rating);
					reviewsRatingSum += rating;
                    link = val.link;
                    title = val.title;
                    userlink = val.author.link;
                    username = val.author.username;
                    added = val.added;
					
					
					var dateArray = added.split(/[- :]/),
					addeddate = new Date(dateArray[0], dateArray[1]-1, dateArray[2], dateArray[3], dateArray[4], dateArray[5]);
					var curr_date = addeddate.getDate();
					var curr_month = addeddate.getMonth();
					var curr_year = addeddate.getFullYear();
					var formateddate = m_names[curr_month] + " " + curr_date + ", " + + curr_year;  
					
                    long_description = val.long_description;
                    link = val.link;
                    fullstarimage = '<img src="' + fullstarimagelocation + '" alt="*"/>';
                    halfstarimage = '<img src="' + halfstarimagelocation + '" alt="*"/>';
                    fullstars = '';
                    halfstars = '';
                    for (i = 1; i <= parseInt(rating / 2, 10); i++) {
                        fullstars = fullstars + fullstarimage;
                    }
                    if (parseInt(rating / 2, 10) != parseFloat(rating / 2)) {
                        halfstars += halfstarimage;
                    }
                    rankingstr = fullstars + halfstars;
					
                    if (username == 'non-member') {
                        texttobereplaced = texttobereplaced + '<div class="n49reviews">' + '<div class="reviews_stars">' + rankingstr + '</div>' +  '<div class="n49reviewstitle"><a href="' + link + '" target="_blank">' + title + '</a>&emsp;</div>' + '<div class="n49reviewsdate">' + formateddate + '</div>' + '<div class="n49reviewLongDesc">' + long_description + '</div>' + '</div>';
                    } else {
                        texttobereplaced = texttobereplaced + '<div class="n49reviews">' + '<div class="reviews_stars">' + rankingstr + '</div>' +  '<div class="n49reviewstitle"><a href="' + link + '" target="_blank">' + title + '</a>&emsp;</div>' + '<div class="n49reviewsdate">' + formateddate + '</div>' + '<div class="n49reviewsuser"><span>By: </span><font style="text-decoration:underline;">' + username + '</font></div>' + '<div class="n49reviewLongDesc">' + long_description + '</div>' + '</div>';
                    }
                });
				if (texttobereplaced != ''){
					$("#reviews-wrap").html(texttobereplaced);
				}
				
				fullstarimagelocationForTotal = '/static/images/star-big.png';
				halfstarimagelocationForTotal = '/static/images/halfstar-big.png';
				fullstarimage = '<img src="' + fullstarimagelocationForTotal + '" alt="*"/>';
				halfstarimage = '<img src="' + halfstarimagelocationForTotal + '" alt="*"/>';
				fullstars = '';
				halfstars = '';
				reviewsRatingAverageFloat =  (reviewsRatingSum / reviewsCount) / 2
                reviewsRatingAverageFloatOst = (reviewsRatingSum / reviewsCount) / 2 - (parseInt(reviewsRatingSum / reviewsCount / 2, 10))
				reviewsRatingAverage = parseInt(reviewsRatingSum / reviewsCount, 10)
				for (i = 1; i <= parseInt(reviewsRatingAverageFloat, 10); i++) {
					fullstars = fullstars + fullstarimage;
				}
                if (parseInt(reviewsRatingAverageFloat, 10) != 5){
                    if (reviewsRatingAverageFloatOst > 0.74){
                        fullstars = fullstars + fullstarimage;
                    }else if (reviewsRatingAverageFloatOst > 0.24){
                        halfstars += halfstarimage;
                    }
                }
				reviewStars = fullstars + halfstars;
				
				
				$("#reviewsCount").html(reviewsCount + " Reviews");
				$("#reviewsAverageStar").html(reviewStars);
				
				
				
}

var reviewsCount = 0;
var reviewsRatingSum = 0;
var reviewStars = '';
initJQuery();