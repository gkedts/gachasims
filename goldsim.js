//A JavaScript-ish implementation of the golden capsule pull simulator.
//TODO: make heroes, nums, and probs not hard-coded, in case they change on us.

var heroes = ["Black Panther", "Black Widow", "Bucky Barnes", "Captain America", "Enchantress", "Falcon", "Hawkeye", "Hulk", "Iron Man", "J.O.C.A.S.T.A", "Loki", "Mockingbird", "Maria Hill", "Ms. Marvel", "Phil Coulson", "Quake", "Red Hulk", "Spider-Woman", "Thor", "Tigra", "Valkyrie", "Vision", "War Machine", "Wasp", "Wiccan", "Winter Soldier","Rick Jones","Skaar"]
var nums = {3:26,5:26,8:26,10:26,30:28};  //number of heroes in each tier; used for odds
var probs = [0.35,0.25,0.2,0.15,0.05];

var Tier = function(value, heroes) {  //handle each tier 3/5/8/10/30 as separate object
  this.value = value;
  this.heroes = heroes;
  }

function generateTiers(nums) {
  var i, tiers = [];
  for (i in nums) {
    Logger.log(i);
    tiers.push(new Tier(i,nums[i]));
  }
  return tiers;
}
  
function weightedRand(tiers,probs) {    //selects tier (3,5,8,10,30) by weighted probability
  var i, sum = 0, r = Math.random();
  for (i in probs) {
    sum += probs[i];
    if (r <= sum) {
      return tiers[i];
      }
  }
}

function uniformRand(array) {   //selects random hero from tier with equal probability
  return array[Math.floor(Math.random() * array.length)];
}

function gimmeShard() {
  tiers = generateTiers(nums);
  T = weightedRand(tiers,probs);    //T.value returns the # of shards (3/5/8/10,30)
  H = uniformRand(heroes.slice(0,T.heroes));    //H is the name of a hero

  //TODO: output the hero we collected, along with the number of shards
}
