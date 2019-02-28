---
author: "hackfox"
date: 2018-01-10 19:31:08
title: "Laravel定时任务"
categories:
  - Development
tags:
  - Laravel
  - php
comments: false
toc: true
draft: false
---


- 定时任务传入参数和选择值方法
  * param为必填
  * option为可选项·

```php
<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;

class TestDemo extends Command {
    /**
     * 控制台命令名称
     *
     * @var string
     */
    protected $signature = 'test {param1} {--param2=}';

    /**
     * 控制台命令描述
     *
     * @var string
     */
    protected $description = 'test';


    /**
     * 创建新的命令实例
     *
     * @param  DripEmailer  $drip
     * @return void
     */
    public function __construct(DripEmailer $drip)
    {
        parent::__construct();
    }

    /**
     * 执行控制台命令
     *
     * @return mixed
     */
    public function handle()
    {
        //参数调用方法
        $param1 = $this->argument('param1');
        $param2 = $this->option('param2');
        $this->info($param1);
        $this->info($param2);
    }
}
```

- 依赖的服务要注入

```php
<?php

namespace App\Console\Commands;

use App\User;
use App\DripEmailer;
use Illuminate\Console\Command;

class SendEmails extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'email:send {user}';

    // Optional argument...
    // email:send {user?}

    // Optional argument with default value...
    // email:send {user=foo}

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Send drip e-mails to a user';

    /**
     * The drip e-mail service.
     *
     * @var DripEmailer
     */
    protected $drip;

    /**
     * Create a new command instance.
     *
     * @param  DripEmailer  $drip
     * @return void
     */
    public function __construct(DripEmailer $drip)
    {
        parent::__construct();

        $this->drip = $drip;
    }

    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {
        $this->drip->send(User::find($this->argument('user')));
    }
}
```

- 回调定时任务

```php
<?php

Route::get('/foo', function () {
    Artisan::queue('email:send', [
        'user' => 1, '--queue' => 'default'
    ]);

    //
});
```

- 一个定时任务回调另一个定时任务

```php
<?php

/**
 * Execute the console command.
 *
 * @return mixed
 */
public function handle()
{
    $this->call('email:send', [
        'user' => 1, '--queue' => 'default'
    ]);

    //
}

```

- 队列执行

```php
<?php

Artisan::queue('email:send', [
    'user' => 1, '--queue' => 'default'
])->onConnection('redis')->onQueue('commands');
```

- Prompting For Input

```php
<?php

/**
 * Execute the console command.
 *
 * @return mixed
 */
public function handle()
{
    $name = $this->ask('What is your name?');
    $password = $this->secret('What is the password?');
    if ($this->confirm('Do you wish to continue?')) {
    //
    }
    $name = $this->choice('What is your name?', ['Taylor', 'Dayle'], $default);
    $this->info('Display this on the screen');
    $this->error('Something went wrong!');
    $this->line('Display this on the screen');

    $headers = ['Name', 'Email'];

    $users = App\User::all(['name', 'email'])->toArray();

    $this->table($headers, $users);
}
```
