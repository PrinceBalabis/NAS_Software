static msg_t ExampleSendThread(void *arg) {

  while (1) {

    // Read tweet sent from python program on computer through serial
    if (Serial.available() > 0) {
      
      String tweet;
      
      while (Serial.available() > 0) {
        chThdSleepMilliseconds(5);
        char c = (char)Serial.read();
//        Serial.println(c);
        tweet = String(c);
        Serial.println(tweet);
      }

      if (tweet.indexOf("room") >= 0) {
        executeCommand = twitterMainLights;
        chSemSignal(&cmdExSem);
      } else if (tweet == "" ) {
        // This happens if serial could not be read
        executeCommand = twitterPaintingLights;
        chSemSignal(&cmdExSem);
      } else {
        executeCommand = twitterSpeakerPower;
        chSemSignal(&cmdExSem);
      }
    }

    chThdSleepMilliseconds(100); // Redo this send program every few moments, give enough time for other threads to run
  }
  return 0;
}
