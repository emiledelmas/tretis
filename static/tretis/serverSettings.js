
/*

  * Config file for the node server
  * Change the ip to yours to make it run on your computer
  * Set localhost to run it locally

*/

const ip = 'hcl0ud.ddns.net'; // Set you IP here
const port = '3000'; // 3000 is the recommanded port for node (change only if you're sure)

/* Don't change that */
if(typeof(module) !== 'undefined') {
  module.exports.ip = ip;
  module.exports.port = port;
}
