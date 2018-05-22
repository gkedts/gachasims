// JS implementation of convolution operation
// Returns an array where the nth value refers to the probability of getting n shards,
// e.g conv[10] returns the probability of getting 10 shards.
// Capsules opened = [# of times convolve() is called] + 1,
// e.g if you call convolve() once, you've opened 2 capsules, if you call twice, you open 3, etc.

function convolve(array1,array2) {
  var conv = [];
  len1 = array1.length;
  len2 = array2.length;
  for (var i=0; i < len1 + len2 - 1; i++) {
    sum = 0;
    for (var j = Math.max(0,i-len2+1); j <= Math.min(i,len1-1); j++) {
      sum += array1[j]*array2[i-j];
    }
    conv[i] = sum;
  }
  //document.write(conv)
}
