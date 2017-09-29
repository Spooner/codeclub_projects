
#include <FastLED.h>

#define NUM_LEDS 16
#define PIN 6
#define DELAY 250


CRGB leds[NUM_LEDS];  

void setup() {
  FastLED.addLeds<NEOPIXEL, PIN>(leds, NUM_LEDS);
}

void loop() {
  int i;
  for (i = 0; i < NUM_LEDS; i++) {
    leds[i] = CRGB::White;
    FastLED.show();
    delay(DELAY);
    leds[i] = CRGB::Black;
  }
  for (i = NUM_LEDS - 1; i >= 0; --i) {
    leds[i] = CRGB::Red;
    FastLED.show();
    delay(DELAY);
    leds[i] = CRGB::Black;
  }
  for (i = 0; i < NUM_LEDS; ++i) {
    leds[i] = CRGB::Green;
    FastLED.show();
    delay(DELAY);
    leds[i] = CRGB::Black;
  }
  for (i = NUM_LEDS - 1; i >= 0; --i) {
    leds[i] = CRGB::Blue;
    FastLED.show();
    delay(DELAY);
    leds[i] = CRGB::Black;
  }
}
