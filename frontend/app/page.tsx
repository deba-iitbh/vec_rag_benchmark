import Header from "@/app/components/header";
import Footer from "@/app/components/footer";
import ChatSection from "./components/chat-section";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center gap-10 p-24 background-gradient">
      <Header />
      <ChatSection />
      <Footer />
    </main>
  );
}
