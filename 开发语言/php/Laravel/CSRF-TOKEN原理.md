#### 用处
- 在Kernel文件内引入的VerifyCsrfToken文件，如果不需要就注释掉
- 传统Form表单提交，在form表单内添加
```
<input name="_token" type="hidden" value="{{ csrf_token() }}" />
```
- 在Ajax，用  X-CSRF-TOKEN或者X-XSRF-TOKEN.在公共父页面添加
```
<meta name="csrf-token" content="{{csrf_token()}}" />
$.ajaxSetup({
  headers: {
    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
  }
});
```

- 判断及添加token源码,在Illuminate\Foundation\Http\Middleware\VerifyCsrfToken文件内
```php
  public function handle($request, Closure $next)
  {
        if (
            $this->isReading($request) ||
            $this->runningUnitTests() ||
            $this->shouldPassThrough($request) ||
            $this->tokensMatch($request)
        ) {
            return $this->addCookieToResponse($request, $next($request));
        }

        throw new TokenMismatchException;
  }

  protected function tokensMatch($request)
  {
            $sessionToken = $request->session()->token();

            $token = $request->input('_token') ?: $request->header('X-CSRF-TOKEN');

            if (! $token && $header = $request->header('X-XSRF-TOKEN')) {
                $token = $this->encrypter->decrypt($header);
            }

            if (! is_string($sessionToken) || ! is_string($token)) {
                return false;
            }

            return hash_equals($sessionToken, $token);
  }

  protected function addCookieToResponse($request, $response)
  {
              $config = config('session');

              $response->headers->setCookie(
                  new Cookie(
                      'XSRF-TOKEN', $request->session()->token(), Carbon::now()->getTimestamp() + 60 * $config['lifetime'],
                      $config['path'], $config['domain'], $config['secure'], false
                  )
              );

              return $response;
  }
```

#### 流程
- 每次请求都会走中间件
- token中间件来做验证
- 如果为get、head、options请求则直接通过
- 否则，验证请求带来的token和session里的tonken是否一致，不一致直接抛出异常；
- 添加新的session的token
- 接下来往下走

#### 如何生成
- 通过session来生成
