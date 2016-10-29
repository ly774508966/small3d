/*
 *  GetTokens.cpp
 *
 *  Created on: 2014/10/18
 *      Author: Dimitri Kourkoulis
 *     License: BSD 3-Clause License (see LICENSE file)
 */

#include "GetTokens.hpp"

using namespace std;

namespace small3d {

  int getTokens(string input, char sep, string *tokens) {
    size_t curPos = 0;
    int count = 0;

    size_t length = input.length();

    for (size_t idx = 0; idx < length; ++idx) {
      if (input[idx] == sep) {
        ++count;
      }
    }
    ++count;

    for (int idx = 0; idx < count; ++idx) {
      if (idx == count - 1) {
        tokens[idx] = input.substr(curPos);
      }
      else {

        size_t foundPos = input.find(sep, curPos);
        tokens[idx] = input.substr(curPos, foundPos - curPos);
        curPos = foundPos + 1;
      }
    }
    return count;
  }
}
