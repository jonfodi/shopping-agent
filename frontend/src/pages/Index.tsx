import { useState } from "react";
import { ShoeForm, ShoeFormData } from "@/components/ShoeForm";
import { ShoeResults } from "@/components/ShoeResults";
import { useToast } from "@/hooks/use-toast";
import heroImage from "@/assets/hero-shoes.jpg";

interface ShoeRecommendation {
  name: string;
  category: string;
  price: string | null;
  product_code: string | null;
  colors: string[];
  sizes: string[];
  availability: string | null;
  url: string;
  rank: number;
  size_match: boolean;
}

const Index = () => {
  const [recommendations, setRecommendations] = useState<ShoeRecommendation[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const { toast } = useToast();

  const handleFormSubmit = async (formData: ShoeFormData) => {
    setIsLoading(true);
    try {
      const response = await fetch("http://localhost:8000/run_graph", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setRecommendations(data || []);
      
      toast({
        title: "Success!",
        description: `Found ${data?.length || 0} shoe recommendations`,
      });
    } catch (error) {
      console.error("Error fetching recommendations:", error);
      toast({
        title: "Error",
        description: "Failed to fetch recommendations. Please check if the server is running on localhost:8000",
        variant: "destructive",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Hero Section */}
      <div className="relative overflow-hidden bg-gradient-hero">
        <div className="absolute inset-0">
          <img
            src={heroImage}
            alt="Nike Shoes Hero"
            className="w-full h-full object-cover opacity-20"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-primary/80 to-transparent" />
        </div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24">
          <div className="text-center">
            <h1 className="text-4xl sm:text-6xl font-bold text-white mb-6">
              Find Your Perfect
              <span className="block text-accent">Nike Shoes</span>
            </h1>
            <p className="text-xl text-gray-200 max-w-3xl mx-auto mb-8">
              Our AI-powered shopping agent searches through Nike's entire catalog 
              to find shoes that match your style, size, and budget perfectly.
            </p>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <ShoeForm onSubmit={handleFormSubmit} isLoading={isLoading} />
        
        {recommendations.length > 0 && (
          <ShoeResults recommendations={recommendations} />
        )}
      </div>
    </div>
  );
};

export default Index;