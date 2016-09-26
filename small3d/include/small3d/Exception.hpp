/*
 *  Exception.hpp
 *
 *  Created on: 2014/10/18
 *      Author: Dimitri Kourkoulis
 *     License: BSD 3-Clause License (see LICENSE file)
 */

#pragma once

#include <exception>
#include <string>

using namespace std;

namespace small3d {

  /**
   * @class Exception
   * @brief The standard exception for small3d.
   */

  class Exception : public exception  {
  private:
    string message;
  public:

    /**
     * @brief Default constructor.
     */

    Exception();

    /**
     * @brief Constructor with message.
     *
     * @param	message	The message.
     */

    Exception(string message);

    /**
     * @brief Returns a null terminated character sequence that can be used to identify the exception.
     *
     * @return	Information about the exception.
     */

    virtual const char* what() const throw();

    /**
     * Destructor.
     */

    virtual ~Exception() throw();
  };

}
