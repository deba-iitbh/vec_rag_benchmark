import Image from "next/image";

export default function Footer() {
  return (
    <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
      <p className="fixed left-0 top-0 flex w-full justify-center pb-6 pt-8 dark:from-inherit sm:static lg:w-auto lg:p-4">
        Copyright © 2024
      </p>
      <p className="fixed left-0 top-0 flex w-full justify-center pb-6 pt-8 dark:from-inherit sm:static lg:w-auto lg:p-4">
        <a
          href="https://www.llamaindex.ai/"
          className="flex items-center justify-center gap-2"
        >
        Built with
          <Image
            className="rounded-xl"
            src="/llama.png"
            alt="Llama Logo"
            width={25}
            height={25}
            priority
          />
        </a>
        </p>
    </div>
  );
}
