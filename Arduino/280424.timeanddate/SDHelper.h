#include "Arduino.h"
#include "WString.h"
class SDHelper {
public:
  int GPS_Year;
  int GPS_Month;
  int GPS_Day;

  int GPS_Hour;
  int GPS_Minute;
  int GPS_Second;

  double Lat;
  double Lng;

public:
  String Date() {
    return String(GPS_Day) + ":" + String(GPS_Month) + ":" + String(GPS_Year);
  }

  String Time_HMS(int TZ) {
    ConvertToLocalTime(GPS_Hour, TZ);

    String timeString = "";
    // Save time to string
    if (GPS_Hour < 10) timeString += "0";
    timeString += String(GPS_Hour) + ":";
    if (GPS_Minute < 10) timeString += "0";
    timeString += String(GPS_Minute) + ":";
    if (GPS_Second < 10) timeString += "0";
    timeString += String(GPS_Second);

    return timeString;
  }

  void ConvertToLocalTime(int& hour, int TZ) {
    hour += TZ;
    if (hour >= 24) hour -= 24;
  }
};