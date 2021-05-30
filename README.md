# spotify-api
Spotify API operation code for python

## Description
This code can control Spotify API on python.
By using Spotify API, you accept the Spotify Developer Terms of Service.
When you use this codes, you need to input 'client ID' and 'client secret'
In this codes,'client ID' and 'client secret' are written like '0000000000000000000000'
This repository contain 5 files.  
・spotyfy_api_track_data_feature.py  
Track feature parameters of one track can be obtained by this code.   
  
・spotyfy_api_track_data_for_musician.py  
Track feature parameters of one track can be obtained by this code.   
In particular, these parameters is usefull when you play a cover of the track.  
  
・spotyfy_api_playlist_track_feature.py   
Track feature parameters from one playlist can be obtained.
And track feature parameters saved in csv file by this code.  
  
・spotyfy_api_const_bpm_playlist_creation.py  
Playlist which have constant BPM tracks can be created.
  
・spotyfy_api_const_bpm_playlist_addition.py  
Constant BPM tracks can be added in created playlist.  
  
## Install
This code use External python library.  
Before You use code, you need to install 'spotipy' and 'pandas' library.  
  
## Licence
You can use for free.  
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
  
# for Japanese

このコードはPython向けに書かれたコードです。  
Spotify APIを操作するためのコードです。  

Spotify APIを使うためには、Spotify Developer Termsに別途登録する必要があります。  
このコードを使用するには、'client ID' と 'client secret'を入力する必要があります。  
'client ID' と 'client secret'はSpotify Developer Termsに登録することで取得することが出来ます。  
このコード上では、'client ID' と 'client secret'は0000000000000000000000と表現されています。  
このリポジトリには５つのファイルがあります。  
  
・spotyfy_api_track_data_feature.py  
単一曲の特徴パラメーターを取得することが出来ます。  
・spotyfy_api_track_data_for_musician.py  
単一曲のパラメーターのうち、曲をカバーする際に有用なデータを取得することが出来ます。  
・spotyfy_api_playlist_track_feature.py  
プレイリストの曲の特徴パラメータを取得して一覧をCSVファイルで保存します。  
・spotyfy_api_const_bpm_playlist_creation.py  
一定のBPMを持つ曲のプレイリストを作成します。  
・spotyfy_api_const_bpm_playlist_addition.py  
一定のBPMを持つ曲を作成済みプレイリストに追加します。  
  
このコードは、外部ライブラリとして「spotipy」と「pandas」を使用しています。  
コードを実行する前に、上記ライブラリをインストールする必要があります。  
ライセンスフリーでご自由にご利用いただけます。  著作権表示等も不要です。  
作者または著作権者は、契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに起因または関連し、あるいはソフトウェアの使用またはその他の扱いによって生じる一切の請求、損害、その他の義務について何らの責任も負わないものとします。 
