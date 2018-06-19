# PyGogol
An auto-generated wrapper for Google's various APIs (inspired by [gogol for Haskell](https://github.com/brendanhay/gogol))

I hacked this in an afternoon, and it is still very very very rough. Feel free to contribute!

## Usage

```
credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=['https://www.googleapis.com/auth/drive'])
gapi = GoogleAPI(creds)
req = Files.copy("myFileId")
res = gapi.send(req)
```