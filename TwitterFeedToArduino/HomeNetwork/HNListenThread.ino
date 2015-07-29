/**
 *  HMListenThread
 *  Idles until a message is received from a client.
 **/

static msg_t HNListenThread(void *arg) {

  while (1) {
    if (msgReceived) { // Check message if a new message is received
      bool msgSent = false;

      if (msgType == typeCommand) { // If its a simple command
        //Commands here
      } else if (msgType == typeAsk) { // If its a question
        //Questions here
        switch (msgContent) {
          case cmdExampleAskCommand:
            // Send return-message back to client
            homeNetwork.respondToQuestion(msgSender, cmdExampleResponseData);
            break;
        }
      }

      msgReceived = false; // Listen for new message
    }
    chThdSleepMilliseconds(homeNetworkCheckMessageDelay); // Check every few ms if a message is received
  }
  return 0;
}
