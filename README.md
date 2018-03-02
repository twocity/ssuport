## ssuport

  ssuport.py is a simple tool used to show information of [android support libraries](https://developer.android.com/topic/libraries/support-library/features.html)

## Usage
  
  List all support libraries:

  ```shell
  python3 ssuport.py --list
  ```
  Show details of given library name

  ```shell
  python3 ssuport.py --lib=recyclerview-v7
  ```
  output will be:

  ```shell
  com.android.support:recyclerview-v7
  ---------
  LATEST VERSION:     27.1.0
  RELEASE VERSION:    27.1.0
  INSTALL:            implementation 'com.android.support:recyclerview-v7:27.1.0'
  CHANGES:            https://developer.android.com/topic/libraries/support-library/revisions.html
  ```

  Note that the value of option `lib` must be listed in `--list`
