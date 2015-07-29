// This is the nodeID of this Arduino.
// WARNING! DONT FORGET TO SET UNIQUE NODE ID IN config.h FOR EACH NODE!
// If you are creating a new node add it to: "\library\HomeNetwork\homeNetworkNodes.h"
const uint16_t nodeID = nodeNAS;

//Hardware
const uint8_t homeNetworkCEPin = 8;
const uint8_t homeNetworkCSNPin = 9;

//Tweaks
const uint16_t homeNetworkCheckMessageDelay = 40; // How often to check for a new message, WARNING! The shorther the delay the less time for for other threads!

//Twitter actions
const uint8_t twitterMainLights = 1;
const uint8_t twitterSpeakerPower = 2;
const uint8_t twitterPaintingLights = 3;
