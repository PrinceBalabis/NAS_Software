/**
 ** CommandExecutioner thread
 ** Executes commands
 **/

int32_t executeCommand = 0;

// Declare a semaphore with an inital counter value of zero.
SEMAPHORE_DECL(cmdExSem, 0);

static msg_t CommandExecutioner(void *arg)
{

  while (1)
  {
    // Wait for signal from either HNListenThread or Keypad Thread to run this loop
    chSemWait(&cmdExSem);

    switch (executeCommand) {
      case twitterMainLights:
        homeNetwork.toggleMainLights();
        break;
      case twitterSpeakerPower:
        homeNetwork.toggleSpeakerPower();
        break;
      case twitterPaintingLights:
        homeNetwork.togglePaintingLights();
        break;
    }
  }
  return 0;
}
