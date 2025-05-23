<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-2">
    <div class="p-12 bg-white border border-gray-200 rounded-lg">
      <h1 class="mb-6 text-2xl">Login</h1>

      <p class="mb-6 text-gray-500">
        Login to your account to access your dashboard and manage your preferences.
      </p>

      <p class="font-bold">
        Already have an account? <a href="#" class="underline">Click here</a> to log in!
      </p>
    </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6">
          <div>
            <label>E-mail</label><br />
            <input
              type="email"
              placeholder="Your e-mail address"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>
         

          <div>
            <label>Password</label><br />
            <input
              type="password"
              placeholder="Your password"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          

          <div>
            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
