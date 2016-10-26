//Such visualization refer to an online example, which can be accessed here http://bl.ocks.org/NPashaP/96447623ef4d342ee09b
//And we made some modification to feed our own data.

$(document).ready(function() {

var freqData =[
{State:'00',freq:{'LARCENY/THEFT':7019,'OTHER OFFENSES':7375,'NON-CRIMINAL':4305,'ASSAULT':4291,'DRUG/NARCOTIC':1703,'VEHICLE THEFT':2035,'VANDALISM':2681,'WARRANTS':1680,'BURGLARY':1365,'SUSPICIOUS OCC':2033}}
,{State:'01',freq:{'LARCENY/THEFT':4304,'OTHER OFFENSES':3630,'NON-CRIMINAL':2292,'ASSAULT':3789,'DRUG/NARCOTIC':1043,'VEHICLE THEFT':1392,'VANDALISM':1832,'WARRANTS':1205,'BURGLARY':832,'SUSPICIOUS OCC':844}}
,{State:'02',freq:{'LARCENY/THEFT':2957,'OTHER OFFENSES':3057,'NON-CRIMINAL':1789,'ASSAULT':3454,'DRUG/NARCOTIC':808,'VEHICLE THEFT':1116,'VANDALISM':1819,'WARRANTS':977,'BURGLARY':879,'SUSPICIOUS OCC':793}}
,{State:'03',freq:{'LARCENY/THEFT':1786,'OTHER OFFENSES':2003,'NON-CRIMINAL':1240,'ASSAULT':1738,'DRUG/NARCOTIC':546,'VEHICLE THEFT':669,'VANDALISM':1107,'WARRANTS':694,'BURGLARY':865,'SUSPICIOUS OCC':553}}
,{State:'04',freq:{'LARCENY/THEFT':1098,'OTHER OFFENSES':1516,'NON-CRIMINAL':941,'ASSAULT':1052,'DRUG/NARCOTIC':379,'VEHICLE THEFT':505,'VANDALISM':711,'WARRANTS':567,'BURGLARY':772,'SUSPICIOUS OCC':366}}
,{State:'05',freq:{'LARCENY/THEFT':1130,'OTHER OFFENSES':1166,'NON-CRIMINAL':861,'ASSAULT':825,'DRUG/NARCOTIC':205,'VEHICLE THEFT':498,'VANDALISM':579,'WARRANTS':399,'BURGLARY':707,'SUSPICIOUS OCC':287}}
,{State:'06',freq:{'LARCENY/THEFT':1806,'OTHER OFFENSES':1692,'NON-CRIMINAL':1541,'ASSAULT':1034,'DRUG/NARCOTIC':600,'VEHICLE THEFT':741,'VANDALISM':661,'WARRANTS':715,'BURGLARY':805,'SUSPICIOUS OCC':468}}
,{State:'07',freq:{'LARCENY/THEFT':2930,'OTHER OFFENSES':3459,'NON-CRIMINAL':2758,'ASSAULT':1580,'DRUG/NARCOTIC':1313,'VEHICLE THEFT':1268,'VANDALISM':932,'WARRANTS':1337,'BURGLARY':1272,'SUSPICIOUS OCC':793}}
,{State:'08',freq:{'LARCENY/THEFT':4952,'OTHER OFFENSES':5264,'NON-CRIMINAL':3886,'ASSAULT':2573,'DRUG/NARCOTIC':1733,'VEHICLE THEFT':2002,'VANDALISM':1395,'WARRANTS':1591,'BURGLARY':2124,'SUSPICIOUS OCC':1409}}
,{State:'09',freq:{'LARCENY/THEFT':5650,'OTHER OFFENSES':6010,'NON-CRIMINAL':4545,'ASSAULT':2847,'DRUG/NARCOTIC':2114,'VEHICLE THEFT':1868,'VANDALISM':1295,'WARRANTS':1839,'BURGLARY':1794,'SUSPICIOUS OCC':1574}}
,{State:'10',freq:{'LARCENY/THEFT':6924,'OTHER OFFENSES':5857,'NON-CRIMINAL':5003,'ASSAULT':3164,'DRUG/NARCOTIC':2422,'VEHICLE THEFT':1793,'VANDALISM':1356,'WARRANTS':2077,'BURGLARY':1646,'SUSPICIOUS OCC':1556}}
,{State:'11',freq:{'LARCENY/THEFT':7688,'OTHER OFFENSES':5800,'NON-CRIMINAL':4931,'ASSAULT':3368,'DRUG/NARCOTIC':2733,'VEHICLE THEFT':1508,'VANDALISM':1267,'WARRANTS':2079,'BURGLARY':1610,'SUSPICIOUS OCC':1560}}
,{State:'12',freq:{'LARCENY/THEFT':10160,'OTHER OFFENSES':7702,'NON-CRIMINAL':6761,'ASSAULT':4207,'DRUG/NARCOTIC':2696,'VEHICLE THEFT':2313,'VANDALISM':1770,'WARRANTS':2276,'BURGLARY':2102,'SUSPICIOUS OCC':2364}}
,{State:'13',freq:{'LARCENY/THEFT':8999,'OTHER OFFENSES':6378,'NON-CRIMINAL':5329,'ASSAULT':3648,'DRUG/NARCOTIC':3593,'VEHICLE THEFT':1646,'VANDALISM':1338,'WARRANTS':2432,'BURGLARY':1404,'SUSPICIOUS OCC':1653}}
,{State:'14',freq:{'LARCENY/THEFT':9229,'OTHER OFFENSES':6375,'NON-CRIMINAL':5284,'ASSAULT':3682,'DRUG/NARCOTIC':4046,'VEHICLE THEFT':1973,'VANDALISM':1506,'WARRANTS':2449,'BURGLARY':1514,'SUSPICIOUS OCC':1723}}
,{State:'15',freq:{'LARCENY/THEFT':10164,'OTHER OFFENSES':6720,'NON-CRIMINAL':5595,'ASSAULT':4154,'DRUG/NARCOTIC':3758,'VEHICLE THEFT':2231,'VANDALISM':1777,'WARRANTS':2468,'BURGLARY':1763,'SUSPICIOUS OCC':1859}}
,{State:'16',freq:{'LARCENY/THEFT':10564,'OTHER OFFENSES':7559,'NON-CRIMINAL':5602,'ASSAULT':4010,'DRUG/NARCOTIC':3971,'VEHICLE THEFT':2732,'VANDALISM':2008,'WARRANTS':2679,'BURGLARY':1999,'SUSPICIOUS OCC':1811}}
,{State:'17',freq:{'LARCENY/THEFT':11753,'OTHER OFFENSES':7719,'NON-CRIMINAL':5088,'ASSAULT':4147,'DRUG/NARCOTIC':4011,'VEHICLE THEFT':3569,'VANDALISM':2726,'WARRANTS':2776,'BURGLARY':2609,'SUSPICIOUS OCC':1708}}
,{State:'18',freq:{'LARCENY/THEFT':13875,'OTHER OFFENSES':6959,'NON-CRIMINAL':4876,'ASSAULT':4025,'DRUG/NARCOTIC':3619,'VEHICLE THEFT':4418,'VANDALISM':3204,'WARRANTS':2495,'BURGLARY':2574,'SUSPICIOUS OCC':1615}}
,{State:'19',freq:{'LARCENY/THEFT':12912,'OTHER OFFENSES':6132,'NON-CRIMINAL':4256,'ASSAULT':3940,'DRUG/NARCOTIC':3156,'VEHICLE THEFT':3807,'VANDALISM':2829,'WARRANTS':2169,'BURGLARY':1931,'SUSPICIOUS OCC':1471}}
,{State:'20',freq:{'LARCENY/THEFT':10984,'OTHER OFFENSES':5335,'NON-CRIMINAL':3906,'ASSAULT':3841,'DRUG/NARCOTIC':2377,'VEHICLE THEFT':4018,'VANDALISM':2908,'WARRANTS':1709,'BURGLARY':1631,'SUSPICIOUS OCC':1261}}
,{State:'21',freq:{'LARCENY/THEFT':9600,'OTHER OFFENSES':5470,'NON-CRIMINAL':3940,'ASSAULT':3978,'DRUG/NARCOTIC':2278,'VEHICLE THEFT':3965,'VANDALISM':3056,'WARRANTS':1690,'BURGLARY':1579,'SUSPICIOUS OCC':1338}}
,{State:'22',freq:{'LARCENY/THEFT':9507,'OTHER OFFENSES':6574,'NON-CRIMINAL':3951,'ASSAULT':3885,'DRUG/NARCOTIC':2585,'VEHICLE THEFT':4145,'VANDALISM':3144,'WARRANTS':2039,'BURGLARY':1541,'SUSPICIOUS OCC':1265}}
,{State:'23',freq:{'LARCENY/THEFT':8909,'OTHER OFFENSES':6430,'NON-CRIMINAL':3624,'ASSAULT':3644,'DRUG/NARCOTIC':2282,'VEHICLE THEFT':3569,'VANDALISM':2824,'WARRANTS':1872,'BURGLARY':1437,'SUSPICIOUS OCC':1110}}
];



dashboard('#dashboard',freqData);
function dashboard(id, fData){
    // var barColor = '#75a3a3';
  var barColor = 'steelblue';


'LARCENY/THEFT','OTHER OFFENSES','NON-CRIMINAL','ASSAULT','DRUG/NARCOTIC'
        ,'VEHICLE THEFT','VANDALISM','WARRANTS','BURGLARY','SUSPICIOUS OCC'
    // function segColor(c){ return {'LARCENY/THEFT':"#807dba", 'OTHER OFFENSES':"#e08214",'Fashion':"#339933",'Technology':"#FF99CC",'Sports': "darkgrey"}[c]; }
     function segColor(c){ return {'LARCENY/THEFT':"#FF6600", 'OTHER OFFENSES':"#ffcc80",'NON-CRIMINAL':"#FF9999",'ASSAULT':"#cc6699",'DRUG/NARCOTIC': "#B80075"
     ,'VEHICLE THEFT':"#807dba",'VANDALISM':"#e08214",'WARRANTS':"#339933",'BURGLARY':"#FF99CC",'SUSPICIOUS OCC':"darkgrey"}[c]; }   

    fData.forEach(function(d){d.total=d.freq['LARCENY/THEFT']+d.freq['OTHER OFFENSES']+d.freq['NON-CRIMINAL']+d.freq['ASSAULT']+d.freq['DRUG/NARCOTIC']
        +d.freq['VEHICLE THEFT']+d.freq['VANDALISM']+d.freq['WARRANTS']+d.freq['BURGLARY']+d.freq['SUSPICIOUS OCC'];});
    
    function histoGram(fD){
        var hG={},    
            hGDim = {t: 30, r: 0, b: 30, l: 30};
            hGDim.w = 1000 - hGDim.l - hGDim.r, 
            hGDim.h = 300 - hGDim.t - hGDim.b;
            
        var hGsvg = d3.select(id).append("svg")
            .attr("width", hGDim.w + hGDim.l + hGDim.r)
            .attr("height", hGDim.h + hGDim.t + hGDim.b).append("g")
            .attr("transform", "translate(" + hGDim.l + "," + hGDim.t + ")");

        var x = d3.scale.ordinal().rangeRoundBands([0, hGDim.w], 0.3)
                .domain(fD.map(function(d) { return d[0]; }));

        hGsvg.append("g").attr("class", "x axis")
            .attr("transform", "translate(0," + hGDim.h + ")")
            .call(d3.svg.axis().scale(x).orient("bottom"));

       
        var y = d3.scale.linear().range([hGDim.h, 0])
                .domain([0, d3.max(fD, function(d) { return d[1]; })]);

  
        var bars = hGsvg.selectAll(".bar").data(fD).enter()
                .append("g").attr("class", "bar");
        
     
        bars.append("rect")
            .attr("x", function(d) { return x(d[0]); })
            .attr("y", function(d) { return y(d[1]); })
            .attr("width", x.rangeBand())
            .attr("height", function(d) { return hGDim.h - y(d[1]); })
            .attr('fill',barColor)
            .on("mouseover",mouseover)
            .on("mouseout",mouseout);
            
        
        bars.append("text").text(function(d){ return d3.format(",")(d[1])})
            .attr("x", function(d) { return x(d[0])+x.rangeBand()/2; })
            .attr("y", function(d) { return y(d[1])-5; })
            .attr("text-anchor", "middle");
        
        function mouseover(d){  
  
            var st = fData.filter(function(s){ return s.State == d[0];})[0],
                nD = d3.keys(st.freq).map(function(s){ return {type:s, freq:st.freq[s]};});
 
            pC.update(nD);
            leg.update(nD);
        }
        
        function mouseout(d){   
  
            pC.update(tF);
            leg.update(tF);
        }
        
  
        hG.update = function(nD, color){
    
            y.domain([0, d3.max(nD, function(d) { return d[1]; })]);
            
     
            var bars = hGsvg.selectAll(".bar").data(nD);
   
            bars.select("rect").transition().duration(500)
                .attr("y", function(d) {return y(d[1]); })
                .attr("height", function(d) { return hGDim.h - y(d[1]); })
                .attr("fill", color);

  
            bars.select("text").transition().duration(500)
                .text(function(d){ return d3.format(",")(d[1])})
                .attr("y", function(d) {return y(d[1])-5; });            
        }        
        return hG;
    }
    

    function pieChart(pD){
        var pC ={},
             pieDim ={w:400, h: 400};
            //  pieDim = {t: 30, r: 0, b: 30, l: 30};
            // pieDim.w = 1000 - pieDim.l - pieDim.r, 
            // pieDim.h = 300 - pieDim.t - pieDim.b;
        pieDim.r = Math.min(pieDim.w, pieDim.h) / 2;

                
   
        var piesvg = d3.select(id).append("svg")
            .attr("width", pieDim.w).attr("height", pieDim.h).append("g")
            .attr("transform", "translate("+pieDim.w/2+","+pieDim.h/2+")");

        var arc = d3.svg.arc().outerRadius(pieDim.r - 10).innerRadius(0);

     
        var pie = d3.layout.pie().sort(null).value(function(d) { return d.freq; });

    
        piesvg.selectAll("path").data(pie(pD)).enter().append("path").attr("d", arc)
            .each(function(d) { this._current = d; })
            .style("fill", function(d) { return segColor(d.data.type); })
            .on("mouseover",mouseover).on("mouseout",mouseout);


 
        pC.update = function(nD){
            piesvg.selectAll("path").data(pie(nD)).transition().duration(500)
                .attrTween("d", arcTween);
        }      

        function mouseover(d){
 
            hG.update(fData.map(function(v){ 
                return [v.State,v.freq[d.data.type]];}),segColor(d.data.type));
        }

        function mouseout(d){
     
            hG.update(fData.map(function(v){
                return [v.State,v.total];}), barColor);
        }
 
        function arcTween(a) {
            var i = d3.interpolate(this._current, a);
            this._current = i(0);
            return function(t) { return arc(i(t));    };
        }    
        return pC;
    }
    

    function legend(lD){
        var leg = {};
            
    
        var legend = d3.select(id).append("table").attr('class','legend');
        
  
        var tr = legend.append("tbody").selectAll("tr").data(lD).enter().append("tr");
            
    
        tr.append("td").append("svg").attr("width", '16').attr("height", '16').append("rect")
            .attr("width", '16').attr("height", '16')
			.attr("fill",function(d){ return segColor(d.type); })
            .on('mouseover',mouseover)
            .on('mouseout',mouseout);

        function mouseover(d){

            hG.update(fData.map(function(v){ 
                return [v.State,v.freq[d.data.type]];}),segColor(d.data.type));
        }

   
        function mouseout(d){

            hG.update(fData.map(function(v){
                return [v.State,v.total];}), barColor);
        }
            
 
        tr.append("td").text(function(d){ return d.type;});

    
        tr.append("td").attr("class",'legendFreq')
            .text(function(d){ return d3.format(",")(d.freq);});

        tr.append("td").attr("class",'legendPerc')
            .text(function(d){ return getLegend(d,lD);});


        leg.update = function(nD){

            var l = legend.select("tbody").selectAll("tr").data(nD);
            l.select(".legendFreq").text(function(d){ return d3.format(",")(d.freq);});
            l.select(".legendPerc").text(function(d){ return getLegend(d,nD);});        
        }
        
        function getLegend(d,aD){ 
            return d3.format("%")(d.freq/d3.sum(aD.map(function(v){ return v.freq; })));
        }

        return leg;
    }
    

    var tF = ['LARCENY/THEFT','OTHER OFFENSES','NON-CRIMINAL','ASSAULT','DRUG/NARCOTIC'
        ,'VEHICLE THEFT','VANDALISM','WARRANTS','BURGLARY','SUSPICIOUS OCC'].map(function(d){ 
        return {type:d, freq: d3.sum(fData.map(function(t){ return t.freq[d];}))}; 
    });    
    
    var sF = fData.map(function(d){return [d.State,d.total];});

    var hG = histoGram(sF), 
        pC = pieChart(tF),
        leg= legend(tF);  
}

})